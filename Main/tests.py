from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from .forms import CommentForm, SellForm, UserAddressForm
from .models import Address, Class, Comment, CustomUser, Like, Product, Transaction


class UserAddressFormTests(TestCase):
    def test_valid_post_length(self):
        # 郵便番号が7桁の場合は有効であることを検証する
        params = {
            "post": "1234567",
        }
        form = UserAddressForm(params)
        self.assertTrue(form.is_valid())

    def test_invalid_post_length(self):
        # 郵便番号が7桁ではない場合は無効であることを検証する
        params = {"post": "12345678"}  # 8桁の郵便番号
        form = UserAddressForm(params)
        self.assertFalse(form.is_valid())

    def test_invalid_post_when_non_numeric_post(self):
        params = {"post": "ABCDEFG"}  # 7文字だが数字以外のデータ
        form = UserAddressForm(params)
        self.assertFalse(form.is_valid())


class TestEditAddressView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="12345"
        )
        self.client.login(username="testuser", password="12345")
        self.url = reverse("edit_address", args=[self.user.username])
        self.address = Address.objects.create(
            user=self.user,
            first_name="Test",
            last_name="User",
            post="1000000",
            prefecture="13",
            city="Test City",
            house_number="1-1",
            building="Test Building",
        )

    def test_edit_address_success(self):
        response = self.client.post(
            self.url,
            {
                "first_name": "New Test",
                "last_name": "User",
                "post": "1000001",
                "prefecture": "13",
                "city": "New City",
                "house_number": "1-2",
                "building": "New Building",
            },
        )

        self.address.refresh_from_db()
        self.assertEqual(self.address.first_name, "New Test")
        self.assertEqual(self.address.city, "New City")
        self.assertEqual(self.address.house_number, "1-2")
        self.assertEqual(response.status_code, 302)

    def test_edit_address_failure(self):
        response = self.client.post(
            self.url,
            {
                "first_name": "",
                "last_name": "User",
                "post": "1000001",
                "prefecture": "13",
                "city": "",
                "house_number": "1-2",
                "building": "New Building",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, "user_form", "first_name", "This field is required."
        )
        self.assertFormError(response, "user_form", "city", "This field is required.")


class TestCreateCardView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="12345"
        )
        self.client.login(username="testuser", password="12345")
        self.url = reverse("create_card", args=[self.user.username])

    def test_create_card_success(self):
        response = self.client.post(
            self.url,
            {
                "card_number": "4242424242424242",
                "exp_month": "12",
                "exp_year": "2023",
                "cvc": "123",
            },
        )

        self.assertEqual(response.status_code, 302)

    # まだ短い
    def test_create_card_failure(self):
        self.client.post(
            self.url,
            {
                "card_number": "1234567890123456",
                "exp_month": "12",
            },
        )


class TestPaymentView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="12345"
        )
        self.client.login(username="testuser", password="12345")

        self.url = reverse("payment", args=[self.user.username])

    def test_payment_success(self):
        response = self.client.post(self.url, {"card_number": "0", "amount": "2000"})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("payment_complete"))

    def test_payment_failure(self):
        response = self.client.post(
            self.url,
            {
                "card_number": "1",
                "amount": "2000",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("payment"))


class commentFormTest(TestCase):
    def test_form_has_fields(self):
        form = CommentForm()
        self.assertIn("text", form.fields)

    def test_valid_data(self):
        form_data = {
            "text": "text_text",
        }
        form = CommentForm(form_data)
        self.assertTrue(form.is_valid())


class sellFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Class.objects.create(lecture="社会学I")

    def test_form_has_fields(self):
        form = SellForm()
        self.assertIn("image", form.fields)
        self.assertIn("product_name", form.fields)
        self.assertIn("gakubu_category", form.fields)
        self.assertIn("gakka_category", form.fields)
        self.assertIn("genre", form.fields)
        self.assertIn("lecture", form.fields)
        self.assertIn("condition", form.fields)
        self.assertIn("description", form.fields)
        self.assertIn("responsibility", form.fields)
        self.assertIn("price", form.fields)

    def test_valid_data(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合人間学部",
            "gakka_category": "総合人間学科",
            "lecture": "社会学I",
            "genre": "過去問",
            "condition": "新品・未使用",
            "description": "test_description",
            "responsibility": "着払い（購入者負担）",
            "price": "1000",
        }
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertTrue(form.is_valid())

    def test_invalid_image(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合人間学部",
            "gakka_category": "総合人間学科",
            "lecture": "社会学I",
            "genre": "過去問",
            "condition": "新品・未使用",
            "description": "test_description",
            "responsibility": "着払い（購入者負担）",
            "price": "1000",
        }
        with open("media/uploads/images/icon.py", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertFalse(form.is_valid())
        self.assertIn("image", form.errors)

    def test_invalid_category(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合学部",
            "gakka_category": "総合学科",
            "lecture": "社会学I",
            "genre": "過去問",
            "condition": "新品・未使用",
            "description": "test_description",
            "responsibility": "着払い（購入者負担）",
            "price": "1000",
        }
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertFalse(form.is_valid())
        self.assertIn("gakubu_category", form.errors)
        self.assertIn("gakka_category", form.errors)

    def test_invalid_genre(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合人間学部",
            "gakka_category": "総合人間学科",
            "lecture": "社会学I",
            "genre": "test",
            "condition": "新品・未使用",
            "description": "test_description",
            "responsibility": "着払い（購入者負担）",
            "price": "1000",
        }
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertFalse(form.is_valid())
        self.assertIn("genre", form.errors)

    def test_invalid_condition(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合人間学部",
            "gakka_category": "総合人間学科",
            "lecture": "社会学I",
            "genre": "過去問",
            "condition": "test",
            "description": "test_description",
            "responsibility": "着払い（購入者負担）",
            "price": "1000",
        }
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertFalse(form.is_valid())
        self.assertIn("condition", form.errors)

    def test_invalid_responsibility(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合人間学部",
            "gakka_category": "総合人間学科",
            "lecture": "社会学I",
            "genre": "過去問",
            "condition": "新品・未使用",
            "description": "test_description",
            "responsibility": "test",
            "price": "1000",
        }
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertFalse(form.is_valid())
        self.assertIn("responsibility", form.errors)

    def test_invalid_price(self):
        form_data = {
            "product_name": "test",
            "gakubu_category": "総合人間学部",
            "gakka_category": "総合人間学科",
            "lecture": "社会学I",
            "genre": "過去問",
            "condition": "新品・未使用",
            "description": "test_description",
            "responsibility": "着払い（購入者負担）",
            "price": "999999999999",
        }
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        form_image = {"image": file}
        form = SellForm(form_data, form_image)
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)


class homeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            username="test",
            password="thisistest",
            email="test@example.com",
            user_id="test_id",
        )

    def setUp(self):
        self.client.login(username="test@example.com", password="thisistest")

    def test_login_user(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        self.client.logout()
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login?next=/home/")


class sellViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            username="test",
            password="thisistest",
            email="test@example.com",
            user_id="test_id",
        )

    def setUp(self):
        self.client.login(username="test@example.com", password="thisistest")

    def test_login_user(self):
        response = self.client.get("/sell/")
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        self.client.logout()
        response = self.client.get("/sell/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login?next=/sell/")

    def test_create_product(self):
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        response = self.client.post(
            path="/sell/",
            data={
                "product_name": "test",
                "gakubu_category": "総合人間学部",
                "gakka_category": "総合人間学科",
                "lecture": "社会学I",
                "genre": "過去問",
                "condition": "新品・未使用",
                "description": "test_description",
                "responsibility": "着払い（購入者負担）",
                "price": "1000",
                "image": file,
                "confirm": True,
            },
        )
        new_product = Product.objects.filter(product_name="test").first()
        self.assertIsNotNone(new_product)
        self.assertRedirects(response, "/home/")


class descriptionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open("media/uploads/images/test_icon.png", "rb") as f:
            file = SimpleUploadedFile(
                f.name,
                f.read(),
            )
        cls.user1 = CustomUser.objects.create(
            username="test1",
            email="test1@example.com",
            user_id="test1_id",
            icon=file,
        )
        cls.user1.set_password("thisistest1")
        cls.user1.save()
        cls.user2 = CustomUser.objects.create(
            username="test2",
            password="thisistest2",
            email="test2@example.com",
            user_id="test2_id",
            icon=file,
        )
        cls.classroom = Class.objects.create(lecture="社会学I")
        cls.Address1 = Address.objects.create(
            user=cls.user1,
            post=1111111,
            prefecture="東京都",
            city="1",
            house_number=1,
            building="test",
            phone="1234567890",
        )
        cls.Address2 = Address.objects.create(
            user=cls.user2,
            post=1111111,
            prefecture="東京都",
            city="1",
            house_number=1,
            building="test",
            phone="1234567890",
        )
        cls.pro1 = Product.objects.create(
            product_name="pro1",
            description="description1",
            condition="新品・未使用",
            price=1000,
            image=file,
            gakubu_category="総合人間学部",
            gakka_category="総合人間学科",
            classroom_category=cls.classroom,
            seller=cls.user1,
            genre="過去問",
            responsibility="着払い（購入者負担）",
        )
        cls.pro2 = Product.objects.create(
            product_name="pro2",
            description="description2",
            condition="新品・未使用",
            price=1000,
            image=file,
            gakubu_category="総合人間学部",
            gakka_category="総合人間学科",
            classroom_category=cls.classroom,
            seller=cls.user1,
            genre="過去問",
            responsibility="着払い（購入者負担）",
        )
        cls.pro3 = Product.objects.create(
            product_name="pro3",
            description="description3",
            condition="新品・未使用",
            price=1000,
            image=file,
            gakubu_category="総合人間学部",
            gakka_category="総合人間学科",
            classroom_category=cls.classroom,
            seller=cls.user1,
            genre="過去問",
            responsibility="着払い（購入者負担）",
            is_available=False,
        )
        cls.pro4 = Product.objects.create(
            product_name="pro4",
            description="description4",
            condition="新品・未使用",
            price=1000,
            image=file,
            gakubu_category="総合人間学部",
            gakka_category="総合人間学科",
            classroom_category=cls.classroom,
            seller=cls.user2,
            genre="過去問",
            responsibility="着払い（購入者負担）",
        )
        cls.transaction2 = Transaction.objects.create(
            buyer=cls.user2,
            seller=cls.user1,
            product=cls.pro2,
            deliver_address=cls.Address2,
        )

    def setUp(self):
        self.client.login(username="test1@example.com", password="thisistest1")

    def test_logout_user(self):
        self.client.logout()
        response = self.client.get("/product_description/1/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login?next=/product_description/1/")

    def test_login_seller(self):
        response = self.client.get("/product_description/1/")
        self.assertEqual(response.status_code, 200)

    def test_invalid_product(self):
        response = self.client.get("/product_description/99999/")
        self.assertEqual(response.status_code, 404)

    def test_transaction_product(self):
        response = self.client.get("/product_description/2/")
        self.assertEqual(response.status_code, 200)

    def test_sold_product(self):
        response = self.client.get("/product_description/3/")
        self.assertEqual(response.status_code, 200)

    def test_like_product(self):
        self.client.post(
            reverse("like_product"),
            {"product_pk": 1},
        )
        like = Like.objects.get(user=self.user1, product=self.pro1)
        self.assertIsNotNone(like)

    def test_unlike_product(self):
        Like.objects.create(user=self.user1, product=self.pro1)
        self.client.post(
            reverse("like_product"),
            {"product_pk": 1},
        )
        unlike = Like.objects.filter(user=self.user1, product=self.pro1).first()
        self.assertIsNone(unlike)

    def test_comment_create(self):
        comment = Comment.objects.filter(user=self.user1).first()
        self.assertIsNotNone(comment)
        self.assertEqual(comment.text, "test_comment")
