// Uses jQuery API to change color of tag to red on click

// Ensures that script is exec only after DOM has loaded
$(document).ready(function() {
    // Event listener for when user clicks on the Tag
    $('DIV#red_header').click(function () {
        // update text color of the header element
        $('header').css('color', '#FF0000');
    });
});
