# Generated by Django 5.0.1 on 2024-02-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Main", "0002_alter_address_phone_alter_product_gakka_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="prefecture",
            field=models.CharField(
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
    ]
