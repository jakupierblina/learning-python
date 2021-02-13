
function displayDate() {
  ///alert(Date());

  //document.body.onload = addElement;
addElement ();

}



function addElement () {
  // create a new div element

   $(".notes").append("" +
       "<li>\n" +
       "         <div class=\"rotate-1 yellow-bg\">\n" +
       "           <small>12:03:28 12-04-2014</small>\n" +
       "            <h4>Awesome project</h4>\n" +
       "            <p>The years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>\n" +
       "            <a href=\"#\" class=\"text-danger pull-right\"><i class=\"fa fa-trash-o \"></i></a>\n" +
       "                </div>\n" +
       "            </li>");
}

