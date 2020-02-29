(function quotes() {
            quote = $.getJSON("/api/quote");
            $("#quote").html(quote.text);
            $("#author").html(quote.author);
})(); 