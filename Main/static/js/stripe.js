// JavaScriptを使用して、client secretを取得する
const client_secret = document.getElementById('client_secret').value;

// JavaScriptを使用して、Stripeのインスタンスを作成する
const stripe = Stripe('pk_test_51OZnnyAiXkxmyRDeucSGGEKApynBgv8EeBdFF7IjOnxPtonAH31dmwqktZNmCM4wxs5UmbQXOzjoMQMTWPUql3A000ehqwxHwe');
// クレジットカード入力フォームで使用するElementsを設定し
const elements = stripe.elements();
const cardElement = elements.create('card', {hidePostalCode: true});  // ここでcardElementを定義
cardElement.mount('#payment-element');

// クレジットカード情報が送信された時の処理を記述する
document.getElementById('payment-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    // confirmCardSetupを呼び出して支払い処理を完了させる
    const {error, setupIntent} = await stripe.confirmCardSetup(client_secret, {
        payment_method: {
            card: cardElement,  // ここで使用
        },
    });

    if (error) {
        const messageContainer = document.querySelector('#error-message');
        messageContainer.textContent = error.message;
    } else {
        // SetupIntentのステータスが'succeeded'なら成功
        if (setupIntent.status === 'succeeded') {
            console.log('Card registered successfully!');
            console.log(setupIntent.status)
            // カードの登録が成功すれば"payment_information.html"にリダイレクトするための処理をviews.pyに送信する
            // 隠しフィールドの値を設定
            document.getElementById('stripe_success').value = '1';
            // フォームを送信
            document.getElementById('payment-form').submit();
        }
    }
});
