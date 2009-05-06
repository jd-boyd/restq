<?php

require_once "RESTclient.php";
require_once "msgQ_client.php";

put("phpQ");

for($i = 0 ; $i < 10000 ; $i += 1)
{
  post("phpQ", "phpTest".$i);
}

for($i = 0 ; $i < 10000 ; $i += 1)
{
  //echo "Return ", get("phpQ"), "\n";
  $res=get("phpQ");
}

?>
