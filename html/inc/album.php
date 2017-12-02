<?php
$Path = getcwd();
$LOOPINDEX = 0;
$ALBUMNAME = $_GET['name'];
$PICTURES = array();
//$ALBUMNAME = "Test";
if (!is_string($ALBUMNAME)){
	http_response_code(500);
	die();
}
$FOLDER = dir($_SERVER['DOCUMENT_ROOT']."/static/images/gallery/".$ALBUMNAME);
if(! ($FOLDER instanceof  Directory)){
	http_response_code(500);
	include_once 'html/util/lib.php';
	render('500','.html');
	exit();
}
else {
	$INCS = ['<script src="/static/js/blueimp/blueimp-gallery.js"></script>',
			'<link rel="stylesheet" href="static/css/blueimp/blueimp-gallery-video.css">',
			'<link rel="stylesheet" href="static/css/blueimp/blueimp-gallery-indicator.css">',
			'<link rel="stylesheet" href="static/css/blueimp/blueimp-gallery.min.css">',
			'<script src="/static/js/blueimp/jquery.blueimp-gallery.js"></script>',
			'<script src="/static/js/blueimp/blueimp-gallery-video.js"></script>',
			'<script src="/static/js/blueimp/blueimp-gallery-fullscreen.js"></script>',
			'<script src="/static/js/blueimp/blueimp-gallery-indicator.js"></script>'
			
	];
}
/*	
while (($IMAGE = $FOLDER->read()) !== FALSE){
	if( $IMAGE === "." || $IMAGE ===".."){
		continue;
	}
	if (preg_match_all("/\.(jpe?g|GIF|png)/i", $IMAGE) === 0){
		continue;
	}
	$PICTURES[] = $IMAGE; 
}*/
?>