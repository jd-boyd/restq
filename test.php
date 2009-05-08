<?php

require_once "RESTclient.php";
require_once "msgQ_client.php";

$mq = new msgclient("http://localhost:8990/");

$mq->put("phpQ");

for($i = 0 ; $i < 1000 ; $i += 1)
{
  $mq->post("phpQ", "phpTest".$i);
}

for($i = 0 ; $i < 1000 ; $i += 1)
{
  //echo "Return ", get("phpQ"), "\n";
  $res=$mq->get("phpQ");
}

?>
