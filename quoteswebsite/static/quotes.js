(function quotes() {
            quote = $.getJSON("/api/quote");
            $("#quote").text(quote.text);
            $("#author").text(quote.author);
})(); 