<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form fields
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Process the form data (e.g., send an email)
    $to = "rohaizazira@gmail.com";
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";

    if (mail($to, $subject, $body)) {
        echo json_encode(array('success' => true));
    } else {
        echo json_encode(array('error' => 'Failed to send email'));
    }
} else {
    echo json_encode(array('error' => 'Invalid request method'));
}
?>