<?php

include 'credentials.php';
#header('Content-Type: application/json');
error_reporting(E_ALL);

$suburb = $_GET['suburb'];
$occurrence_type = $_GET['occurrence_type'];
$time = $_GET['time'];
$date = $_GET['date'];
$nearby_location = $_GET['nearby_location']
$stolen_objects = $_GET['stolen_objects']

$conn = new mysqli($servername, $username, $password, $database);
$conn->close();

$Data = array('suburb' => $suburb, 'occurrence_type' => $occurrence_type, 'time' => $time, 'date' => $date, 'nearby_location' => $nearby_location, 'stolen_objects' => $stolen_objects);
echo json_encode($Data);
?>