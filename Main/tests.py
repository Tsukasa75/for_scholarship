from django.test import TestCase,Client
from django.urls import reverse 
from .models import CustomUser,Address
from .forms import UserAddressForm

class UserAddressFormTests(TestCase):
    def test_valid_post_length(self):
        # 郵便番号が7桁の場合は有効であることを検証する
        params = {'post': '1234567',}
        form = UserAddressForm(params)
        self.assertTrue(form.is_valid())

    def test_invalid_post_length(self):
        # 郵便番号が7桁ではない場合は無効であることを検証する
        params = {'post': '12345678'}  # 8桁の郵便番号
        form = UserAddressForm(params)
        self.assertFalse(form.is_valid())

    def test_invalid_post_when_non_numeric_post(self):
        params = {'post': 'ABCDEFG'} # 7文字だが数字以外のデータ
        form = UserAddressForm(params)
        self.assertFalse(form.is_valid())


class TestEditAddressView(TestCase):
    def setUp(self):
        self.client = Client() 
        self.user = CustomUser.objects.create_user(username='testuser',password='12345')
        self.client.login(username='testuser',password='12345')
        self.url = reverse('edit_address', args=[self.user.username])
        self.address = Address.objects.create(user=self.user, first_name='Test', last_name='User', post='1000000', prefecture='13', city='Test City', house_number='1-1', building='Test Building')

    def test_edit_address_success(self):
        response = self.client.post(self.url, {
            'first_name': 'New Test',
            'last_name': 'User',
            'post': '1000001',
            'prefecture': '13',
            'city': 'New City',
            'house_number': '1-2',
            'building': 'New Building'
        })

        self.address.refresh_from_db()
        self.assertEqual(self.address.first_name, 'New Test')
        self.assertEqual(self.address.city, 'New City')
        self.assertEqual(self.address.house_number, '1-2')
        self.assertEqual(response.status_code, 302)

    def test_edit_address_failure(self):
        response = self.client.post(self.url, {
            'first_name': '',
            'last_name': 'User',
            'post': '1000001',
            'prefecture': '13',
            'city': '',
            'house_number': '1-2',
            'building': 'New Building'
        })

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'user_form', 'first_name', 'This field is required.')
        self.assertFormError(response, 'user_form', 'city', 'This field is required.')

class TestCreateCardView(TestCase): 
    def setUp(self): 
        self.client=Client() 
        self.user=CustomUser.objects.create_user(username='testuser',password='12345') 
        self.client.login(username='testuser',password='12345')
        self.url = reverse('create_card', args=[self.user.username])

    def test_create_card_success(self):
        response = self.client.post(self.url, {
            'card_number': '4242424242424242',
            'exp_month': '12',
            'exp_year': '2023',
            'cvc': '123'
        })

        self.assertEqual(response.status_code, 302)

    # まだ短い
    def test_create_card_failure(self):
        response = self.client.post(self.url, {
            'card_number': '1234567890123456',
            'exp_month': '12', 
        })  

class TestPaymentView(TestCase): 
    def setUp(self): 
        self.client=Client() 
        self.user=CustomUser.objects.create_user(username='testuser',password='12345') 
        self.client.login(username='testuser',password='12345')

        self.url = reverse('payment', args=[self.user.username])

    def test_payment_success(self):
       response = self.client.post(self.url, {
           'card_number': '0', 
           'amount': '2000'
       })

       self.assertEqual(response.status_code, 302)
       self.assertRedirects(response, reverse('payment_complete'))

    def test_payment_failure(self):
        response = self.client.post(self.url, {
            'card_number': '1', 
            'amount': '2000',
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('payment'))
