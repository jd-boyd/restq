<?php

require_once "RESTclient.php";

class msgclient {
  public $baseUrl;// = "http://localhost:8990/";

  function __construct($b) {
    print "Construct ".$b."\n";
    $this->baseUrl = $b;
  }

  function get($qName){
    $rest = new RESTclient();
    
    $url = $this->baseUrl."msg/".$qName;
    $rest->createRequest("$url","GET");
    $rest->sendRequest();
    $output = $rest->getResponse();
    return $output;
  }
  
  function put($qName){
    $rest = new RESTclient();
    
    $url = $this->baseUrl.$qName;
    //$url = "http://localhost:8990/".$qName;
    $rest->createRequest("$url","PUT");
    $rest->sendRequest();
    $output = $rest->getResponse();
    return $output;
  }
  
  
  function post($qName, $value){
    $rest = new RESTclient();
    
    //$inputs = array();
    //$inputs["appid"] = "YahooDemo";
    
    $url = "http://localhost:8990/".$qName;
    //$rest->createRequest("$url","POST", $inputs);
    $rest->createRequest("$url","POST", $value);
    $rest->sendRequest();
    $output = $rest->getResponse();
    return $output;
  }
}
?>
