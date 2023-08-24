<?php
  $filename = $_GET['filename'];
  $file = "portal/" . $filename;

  if (file_exists($file)) {
    #echo "File exists: " . $filename . "<br />";
    #echo "File contents: <br />";
    echo file_get_contents($file);
  } else {
    #echo "File not found: " . $filename;
  }
?>