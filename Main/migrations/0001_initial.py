# Generated by Django 5.0.1 on 2024-02-19 05:57

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import Main.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(default="", max_length=20)),
                ("last_name", models.CharField(default="", max_length=20)),
                ("first_name_kana", models.CharField(default="", max_length=20)),
                ("last_name_kana", models.CharField(default="", max_length=20)),
                (
                    "post",
                    models.CharField(
                        max_length=7, validators=[Main.models.validate_postal_code]
                    ),
                ),
                (
                    "prefecture",
                    models.CharField(
                        choices=[
                            ("13", "東京都"),
                            ("14", "神奈川県"),
                            ("11", "埼玉県"),
                            ("12", "千葉県"),
                            ("27", "大阪府"),
                            ("28", "兵庫県"),
                            ("26", "京都府"),
                            ("29", "奈良県"),
                            ("01", "北海道"),
                            ("02", "青森県"),
                            ("03", "岩手県"),
                            ("04", "宮城県"),
                            ("05", "秋田県"),
                            ("06", "山形県"),
                            ("07", "福島県"),
                            ("08", "茨城県"),
                            ("09", "栃木県"),
                            ("10", "群馬県"),
                            ("19", "山梨県"),
                            ("20", "長野県"),
                            ("15", "新潟県"),
                            ("16", "富山県"),
                            ("17", "石川県"),
                            ("18", "福井県"),
                            ("35", "山口県"),
                            ("36", "徳島県"),
                            ("37", "香川県"),
                            ("38", "愛媛県"),
                            ("39", "高知県"),
                            ("40", "福岡県"),
                            ("41", "佐賀県"),
                            ("42", "長崎県"),
                            ("43", "熊本県"),
                            ("44", "大分県"),
                            ("45", "宮崎県"),
                            ("46", "鹿児島県"),
                            ("47", "沖縄県"),
                        ],
                        max_length=2,
                    ),
                ),
                ("city", models.CharField(max_length=50)),
                (
                    "house_number",
                    models.CharField(
                        max_length=50, validators=[Main.models.validate_number]
                    ),
                ),
                ("building", models.CharField(max_length=10)),
                (
                    "phone",
                    models.CharField(
                        max_length=12, validators=[Main.models.validate_number]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lecture", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("stripe_product_id", models.CharField(max_length=100)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("新品・未使用", "新品、未使用"),
                            ("目立った汚れなし", "目立った汚れなし"),
                            ("やや傷、汚れあり", "やや傷、汚れあり"),
                            ("状態が悪い", "状態が悪い"),
                        ],
                        max_length=10,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=0, max_digits=10)),
                ("image", models.ImageField(upload_to="uploads/images/")),
                (
                    "gakubu_category",
                    models.CharField(
                        choices=[
                            ("総合人間学部", "総合人間学部"),
                            ("文学部", "文学部"),
                            ("教育学部", "教育学部"),
                            ("法学部", "法学部"),
                            ("経済学部", "経済学部"),
                            ("理学部", "理学部"),
                            ("医学部", "医学部"),
                            ("薬学部", "薬学部"),
                            ("工学部", "工学部"),
                            ("農学部", "農学部"),
                        ],
                        default="総合人間学部",
                        max_length=20,
                    ),
                ),
                (
                    "gakka_category",
                    models.CharField(
                        choices=[
                            ("総合人間学科", "総合人間学科"),
                            ("人文学科", "人文学科"),
                            ("教育科学科", "教育科学科"),
                            ("経済経営学科", "経済経営学科"),
                            ("理学科", "理学科"),
                            ("医学科", "医学科"),
                            ("人間健康科学科", "人間健康科学科"),
                            ("薬科学科", "薬科学科"),
                            ("薬学科", "薬学科"),
                            ("地球工学科", "地球工学科"),
                            ("建築学科", "建築学科"),
                            ("物理工学科", "物理工学科"),
                            ("電気電子工学科", "電気電子工学科"),
                            ("情報学科", "情報学科"),
                            ("工業化学科", "工業化学科"),
                            ("資源生物科学科", "資源生物科学科"),
                            ("応用生命科学科", "応用生命科学科"),
                            ("地域環境工学科", "地域環境工学科"),
                            ("食料・環境経済学科", "食料・環境経済学科"),
                            ("森林科学科", "森林科学科"),
                            ("食品生物化学科", "食品生物科学科"),
                        ],
                        default="総合人間学科",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_available", models.BooleanField(default=True)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("過去問", "過去問"),
                            ("教科書の解答", "教科書の回答"),
                            ("教科書", "教科書"),
                            ("その他", "その他"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "responsibility",
                    models.CharField(
                        choices=[
                            ("着払い（購入者負担）", "着払い（購入者負担）"),
                            ("送料込み（出品者負担）", "送料込み（出品者負担）"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "classroom_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Main.class",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                ("auth_number", models.IntegerField(blank=True, null=True)),
                ("user_id", models.CharField(max_length=20)),
                (
                    "stripe_customer_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("introduce", models.TextField(blank=True)),
                ("icon", models.ImageField(upload_to="uploads/images/")),
                (
                    "gakubu",
                    models.CharField(
                        choices=[
                            ("総合人間学部", "総合人間学部"),
                            ("文学部", "文学部"),
                            ("教育学部", "教育学部"),
                            ("法学部", "法学部"),
                            ("経済学部", "経済学部"),
                            ("理学部", "理学部"),
                            ("医学部", "医学部"),
                            ("薬学部", "薬学部"),
                            ("工学部", "工学部"),
                            ("農学部", "農学部"),
                        ],
                        default="総合人間学部",
                        max_length=20,
                    ),
                ),
                (
                    "gakka",
                    models.CharField(
                        choices=[
                            ("総合人間学科", "総合人間学科"),
                            ("人文学科", "人文学科"),
                            ("教育科学科", "教育科学科"),
                            ("経済経営学科", "経済経営学科"),
                            ("理学科", "理学科"),
                            ("医学科", "医学科"),
                            ("人間健康科学科", "人間健康科学科"),
                            ("薬科学科", "薬科学科"),
                            ("薬学科", "薬学科"),
                            ("地球工学科", "地球工学科"),
                            ("建築学科", "建築学科"),
                            ("物理工学科", "物理工学科"),
                            ("電気電子工学科", "電気電子工学科"),
                            ("情報学科", "情報学科"),
                            ("工業化学科", "工業化学科"),
                            ("資源生物科学科", "資源生物科学科"),
                            ("応用生命科学科", "応用生命科学科"),
                            ("地域環境工学科", "地域環境工学科"),
                            ("食料・環境経済学科", "食料・環境経済学科"),
                            ("森林科学科", "森林科学科"),
                            ("食品生物化学科", "食品生物化学科"),
                        ],
                        default="総合人間学科",
                        max_length=20,
                    ),
                ),
                ("point", models.IntegerField(default=0)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("delivery_date", models.DateTimeField()),
                ("deliver_fee", models.CharField(max_length=20)),
                ("is_shipped", models.BooleanField(default=False)),
                ("is_received", models.BooleanField(default=False)),
                (
                    "deliver_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="delivered_product",
                        to="Main.address",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Main.product"
                    ),
                ),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bought_product",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sold_product",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "evaluate",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("comment", models.TextField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Main.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Draft",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_published", models.BooleanField(default=False)),
                ("is_created", models.BooleanField(default=False)),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Main.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="Main.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="address",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
