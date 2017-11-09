<?php
$Path = getcwd();
$LOOPINDEX = 0;
$ALBUMNAME = $_GET['name'];
//$ALBUMNAME = "Test";
if (!is_string($ALBUMNAME)){
	http_response_code(500);
	die();
}
elseif(is_dir($FOLDER = dir("static/images/gallery/".$ALBUMNAME))!=FALSE){
	include_once 'html/util/lib.php';
	render('404','.html');
	die();
}
else {
	$INCS = ['<script src="/static/js/blueimp/blueimp-gallery.js"></script>',
			'<link rel="stylesheet" href="static/css/blueimp/blueimp-gallery.min.css">'.
			'<script src="/static/js/blueimp/jquery.blueimp-gallery.js"></script>'
	];
}
?>