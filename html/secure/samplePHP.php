<?php 

//$output = shell_exec("/usr/bin/python ../pyScript.py");
exec("/usr/bin/python ../pyScript.py", $output, $ret_code);
//echo $ret_code;
if($ret_code === 1)
{
	echo "The function didnt work";
}
else
{
	echo "The function worked";
}

?>