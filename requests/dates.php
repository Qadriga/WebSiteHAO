<?php
echo print_r($_SERVER);
$absRoot = $_SERVER['DOCUMENT_ROOT'];
$db = new SQLite3($absRoot."/requests/terms.sqlite3");
$stm = $db->prepare("Select * FROM terms WhERE ddate BETWEEN ?:first AND ?:last ");
if(!is_null($stm)){
	$stm->bindValue("?:first",date('01-m-y') );
}
?>