<?php

function isMobile(){
    if(isset($_SERVER["HTTP_USER_AGENT"])){
	   return preg_match("/(android|avantgo|blackberry|bolt|boost|cricket|docomo|fone|hiptop|mini|mobi|palm|phone|pie|tablet|up\.browser|up\.link|webos|wos)/i", $_SERVER["HTTP_USER_AGENT"]);
    }
    else{
        return False;
    }
}

function search_file($Filename,$ROOT=NULL){
	if(!isset($ROOT)){
		$_ROOT = getcwd();
	}
	else{
		$_ROOT = $ROOT; 
	}
	//if a root is set this will used or the current working directory
	//print $_ROOT;
	$DIR = array_diff(scandir($_ROOT,SCANDIR_SORT_ASCENDING),array('..','.')); // scan dir and remove the dots
	$RES = in_array($Filename, $DIR);
	return $RES;
}
function overwirte_file($FILENAME,$DATA,$INCLUDE_PATH=NULL){
	if (is_null($INCLUDE_PATH)){
		$_ROOT = getcwd();
	}
	else{
		$_ROOT = $INCLUDE_PATH;
	}
	$file = fopen($_ROOT.$FILENAME, "w");
	fwrite($file, $DATA);
	fclose($file);
}
function render($FILE="index",$FILEEXTENTION=".html"){
	$_ROOT = getcwd();
	if(search_file($FILE.".if","html/inc")){
		include 'html/inc/'.$FILE.'.if';
	}
	elseif (search_file($FILE.".php","html/inc")){
		include 'html/inc/'.$FILE.'.php';
	}
	include 'html/util/top.phtml';
	include 'html/util/nav_bar.html';
	include 'html/sites/'.$FILE.$FILEEXTENTION;
	include 'html/util/footer.phtml';
}
?>