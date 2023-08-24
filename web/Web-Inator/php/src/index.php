<?php
$cookie_name = "user";
$cookie_value_normal = "user=public_user,inator_self_destruct=false";
$cookie_expiration = time() + 3600; // set the expiration time to 1 hour from now
$cookie_path = "/"; // set the cookie to be available in the entire domain
$cookie_value_reverse = strrev($cookie_value_normal);
$final_cookie_val = base64_encode($cookie_value_reverse);

setcookie($cookie_name, $final_cookie_val, $cookie_expiration, $cookie_path);


if (isset($_COOKIE["user"]) && $_COOKIE["user"] == "ZXVydD10Y3VydHNlZF9mbGVzX3JvdGFuaSxuaW1kYT1yZXN1") {
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Dr. Doofenshmirtz is Foiled by Perry the Platypus and a BYU Cybersecurity Student</title>
        <style type="text/css">
            body {
                background-color: #4C4C4C;
                color: #FFFFFF;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                margin-top: 50px;
                margin-bottom: 50px;
            }
            p {
                font-size: 24px;
                line-height: 1.5;
                margin-left: 50px;
                margin-right: 50px;
            }
            .img-container {
                text-align: center;
            }
            img {
                width: 600px;
                height: 400px;
                margin-top: 50px;
                margin-bottom: 50px;
            }
        </style>
    </head>
    <body>
        <h1>Dr. Doofenshmirtz Foiled by Perry the Platypus and a BYU Cybersecurity Student!</h1>
        <div class="img-container">
            <img src="perry.png" alt="Perry the Platypus and a BYU Cybersecurity Student">
        </div>
        <p>It was a close call, but Perry the Platypus and a BYU cybersecurity student were able to stop Dr. Doofenshmirtz\'s evil plan to take over BYU with his Inator. Using their expert skills in hacking, they were able to change the client-side cookie that activated the self-destruct button on the Inator. With a loud explosion, the Inator was destroyed and Dr. Doofenshmirtz\'s evil plan was foiled.</p>
        <p>As Dr. Doofenshmirtz was dragged away by the authorities, he could be heard muttering his catchphrase, "Curse you, Perry the Platypus!" But it was too late, and Perry had saved the day once again.</p>
        <p>byuctf{d0of-and-h1s-cl13nt-s1d3-co0k13-4uth3nt1c4t10n}</p>
    </body>
    </html>
    ';
}
else {
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Dr. Doofenshmirtz Takes Over BYU</title>
        <style type="text/css">
            body {
                background-color: #4C4C4C;
                color: #FFFFFF;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                margin-top: 50px;
                margin-bottom: 50px;
            }
            p {
                font-size: 24px;
                line-height: 1.5;
                margin-left: 50px;
                margin-right: 50px;
            }
            .img-container {
                text-align: center;
            }
            img {
                width: 600px;
                height: 400px;
                margin-top: 50px;
                margin-bottom: 50px;
            }
        </style>
    </head>
    <body>
        <h1>Dr. Doofenshmirtz Takes Over BYU with His Inator!</h1>
        <div class="img-container">
            <img src="https://d23.com/app/uploads/2020/08/780w-463h_082820_10-best-inators_8.jpg" alt="Dr. Doofenshmirtz with his Inator">
        </div>
        <p>It\'s the end of the world as we know it! Dr. Heinz Doofenshmirtz, the evil scientist from Danville, has come up with his latest evil scheme to take over BYU with his Inator. With the flip of a switch, he\'ll activate his Inator and turn the entire campus into his evil lair.</p>
        <p>But fear not, dear students and faculty of BYU! Our hero, Perry the Platypus, has been dispatched to put a stop to Dr. Doofenshmirtz\'s evil plan. Will Perry be able to foil the evil doctor\'s plot and save the campus? Only time will tell...</p>
    </body>
    </html>
    ';
}
?>
