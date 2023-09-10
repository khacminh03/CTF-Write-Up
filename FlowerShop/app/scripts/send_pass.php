<?php

$tmpPwd = $argv[1]; // hfjskguz169424518945754926
$wh = $argv[2]; // https://webhook.site/ccaa6f34-75b3-4e18-8584-5a1653a0e0a1

$data = array('tmp_pass' => $tmpPwd); // data = tmpPwd

$ch = curl_init(); // triển khai curl
curl_setopt($ch, CURLOPT_URL, $wh); 
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

$response = curl_exec($ch);
var_dump($response);

curl_close($ch);

?>