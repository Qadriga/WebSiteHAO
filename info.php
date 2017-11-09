<?php
//phpinfo();
print locale_get_default();
$res = setlocale(LC_ALL, "de_DE.utf8");
if (is_bool($res)){
	print $res?'true':'false';
}
else {
	print $res;
}
?>