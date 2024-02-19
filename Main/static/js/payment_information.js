document.addEventListener('DOMContentLoaded', function() {
    const checkbox = document.querySelector('.credit_card');
    const displayCredit = document.querySelector('.displayCredit');
    const checkboxes = document.querySelectorAll('.after2nd');
    const displayTexts = document.querySelectorAll('.displayText');

    checkbox.addEventListener('change', function() {
        if (this.checked) {
                displayCredit.style.display = 'block'; // テキストを表示
            } else {
                displayCredit.style.display = 'none'; // テキストを非表示
            }
    }); /* クレジットカード追加用 */

    checkboxes.forEach((checkbox,index) => {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                displayTexts[index].style.display = 'block'; // テキストを表示
            } else {
                displayTexts[index].style.display = 'none'; // テキストを非表示
            }
        });
    }); /* クレジットカード以外は利用できない */
});

function addBorder(id) {
    var option = document.getElementById(id);
    if (option.querySelector('input').checked) {
        option.style.borderTop = "1px solid black";
        option.style.borderBottom = "1px solid black";
    } else {
        option.style.borderTop = "";
        option.style.borderBottom = "";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.checkbox-round');
    checkboxes.forEach((checkbox, index) => {
        checkbox.addEventListener('change', function() {
            checkboxes.forEach((box, i) => {
                if (box !== checkbox) {
                    box.checked = false;
                    // Remove border of unchecked checkbox
                    addBorder(`option${i + 1}`);
                }
            });
            // Add or remove border of changed checkbox
            addBorder(`option${index + 1}`);
        });
    });
    /* 既存のJavaScriptは省略 */
});
