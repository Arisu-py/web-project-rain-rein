function onItalic() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<i>${selected}<\i>`);
            };
            function onBold() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<b>${selected}<\b>`);
            };
            function onStrike() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<del>${selected}<\del>`);
            };
            function onCenter() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<center>${selected}<\center>`);
            };
            function onHider1line() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<h1>${selected}<\h1>`);
            };
            function onHider2line() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<h2>${selected}<\h2>`);
            };
            function onHider3line() {
              if (textarea.selectionStart == textarea.selectionEnd) {
                return; // ничего не выделено
              }
              let selected = textarea.value.slice(textarea.selectionStart, textarea.selectionEnd);
              textarea.setRangeText(`<h3>${selected}<\h3>`);
            };

            function onKeyboardShotcut(e) {
              if (e.ctrlKey && e.key === "i") {
                onItalic();
              } else if (e.ctrlKey && e.key === "b") {
                onBold();
              } else if (e.ctrlKey && e.key === "s") {
                onStrike();
              } else if (e.ctrlKey && e.key === "l") {
                onCenterline();
              }
            }
            document.addEventListener("keyup", onKeyboardShotcut, false);