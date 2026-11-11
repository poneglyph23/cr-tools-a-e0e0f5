<?php
$x = $_GET['q'];
echo $x;
mysql_query("SELECT * FROM t WHERE a = '" . $x . "'");
function f($a) { return $undefinedVar + $a; }
