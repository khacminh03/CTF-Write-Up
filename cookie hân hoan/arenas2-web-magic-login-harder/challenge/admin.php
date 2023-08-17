<?php
    header('Content-Type: text/html; charset=utf-8');
    session_start();
    if($_SESSION['username'] != null){
    if(isset($_GET['file'])){
        $file = $_GET['file'];
        include($file);
    }
    }
    else{
        die("Only admin can use this");
    }
?>