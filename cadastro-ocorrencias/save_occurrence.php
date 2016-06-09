<?php

#include 'credentials.php';
#header('Content-Type: application/json');
error_reporting(E_ALL);

$suburb = $_POST['suburb'];
$occurrence_type = $_POST['occurrence_type'];
$time = $_POST['time'];
$date = $_POST['date'];
$nearby_location = $_POST['nearby_location']
$stolen_objects = $_POST['stolen_objects']

#$conn = new mysqli($servername, $username, $password, $database);
#$conn->close();

$Data = array('suburb' => $suburb, 'occurrence_type' => $occurrence_type, 'time' => $time, 'date' => $date, 'nearby_location' => $nearby_location, 'stolen_objects' => $stolen_objects);
echo json_encode($Data);
?>
