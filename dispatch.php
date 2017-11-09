<?php
/* this script handels the incomeing request to the files and renders it
 * this avoids a large armount of .php files in one directory 
 * the files in html/inc which has the file extention .if are 
 * interpreted as standad php files for additonal includes in the head section of the 
 * requested page */

include_once 'html/util/lib.php';
if(!array_key_exists("site", $_GET)){
	print "run it as server module";
	die();
}
$REQUEST_FILE = $_GET['site'];
//print $REQUEST_FILE;
if(search_file($REQUEST_FILE.'.phtml',"html/sites")){
	//echo "phtml found";
    render($REQUEST_FILE,'.phtml');
}
elseif(search_file($REQUEST_FILE.'.html',"html/sites")){
	//echo "html found";
    render($REQUEST_FILE,'.html');
}
else{
    echo "<h1>not Found</h1>";
	render('404','.html');
}
