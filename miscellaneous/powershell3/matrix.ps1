# Remember to use PowerShell 7 with a decently sized console!
#
# For more information on virtual terminal sequences see,
# https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences
$runtime  = 500
$bgColor  = "`e[40m"
$fgColor1 = "`e[38;2;234;216;216m" # 117 (u), 108 (l), 108 (l)
$fgColor2 = "`e[38;2;210;160;216m" # 105 (i),  80 (P), 108 (l)
$fgColor3 = "`e[38;2;132;202;190m" #  66 (B), 101 (e),  95 (_)
$fgColor4 = "`e[30m"
$symbolSet= (18..26)+(28..31)+(33..127)
$consoleWidth = $Host.UI.RawUI.WindowSize.Width
$consoleHeight = $Host.UI.RawUI.WindowSize.Height
$minimumColumnValue = -$consoleHeight
$startingColumnValues = New-Object int[] $consoleWidth
$columnValues = $startingColumnValues
for ($i = 0; $i -le $consoleWidth-1; $i++) {
  $columnValues[$i] = ($minimumColumnValue..-1) | Get-Random
}

$array1 = New-Object 'object[,]' $consoleWidth,$consoleHeight
for ($i = 0; $i -le $consoleWidth-1; $i++) {
  for ($j = 0; $j -le $consoleHeight-1; $j++) {
    $seed = $startingColumnValues[$i]+$j+$i*100
    if (($i -eq 10) -and ($j -eq 3)) {$symbol = [char]110}if (($i -eq 11) -and ($j -eq 3)) {$symbol = [char]32}
    if (($i -eq 12) -and ($j -eq 3)) {$symbol = [char]32}if (($i -eq 24) -and ($j -eq 3)) {$symbol = [char]39}
    if (($i -eq 25) -and ($j -eq 3)) {$symbol = [char]101}if (($i -eq 32) -and ($j -eq 3)) {$symbol = [char]123}
    if (($i -eq 33) -and ($j -eq 3)) {$symbol = [char]108}if (($i -eq 34) -and ($j -eq 3)) {$symbol = [char]123}
    if (($i -eq 20) -and ($j -eq 3)) {$symbol = [char]97}if (($i -eq 21) -and ($j -eq 3)) {$symbol = [char]116}
    if (($i -eq 22) -and ($j -eq 3)) {$symbol = [char]72}if (($i -eq 29) -and ($j -eq 3)) {$symbol = [char]115}
    if (($i -eq 30) -and ($j -eq 3)) {$symbol = [char]101}if (($i -eq 15) -and ($j -eq 3)) {$symbol = [char]103}
    if (($i -eq 16) -and ($j -eq 3)) {$symbol = [char]39}if (($i -eq 17) -and ($j -eq 3)) {$symbol = [char]101}
    if (($i -eq 14) -and ($j -eq 3)) {$symbol = [char]111}if (($i -eq 26) -and ($j -eq 3)) {$symbol = [char]116}
    if (($i -eq 27) -and ($j -eq 3)) {$symbol = [char]113}if (($i -eq 28) -and ($j -eq 3)) {$symbol = [char]98}
    if (($i -eq 13) -and ($j -eq 3)) {$symbol = [char]115}if (($i -eq 40) -and ($j -eq 3)) {$symbol = [char]98}
    if (($i -eq 18) -and ($j -eq 3)) {$symbol = [char]108}if (($i -eq 35) -and ($j -eq 3)) {$symbol = [char]97}
    $symbol = $symbolSet | Get-Random -Count 1 -SetSeed $seed | % {[char]$_}
    if (($i -eq 10) -and ($j -eq 3)) {$symbol = [char]102}if (($i -eq 11) -and ($j -eq 3)) {$symbol = [char]99}
    if (($i -eq 12) -and ($j -eq 3)) {$symbol = [char]116}if (($i -eq 24) -and ($j -eq 3)) {$symbol = [char]110}
    if (($i -eq 25) -and ($j -eq 3)) {$symbol = [char]110}if (($i -eq 32) -and ($j -eq 3)) {$symbol = [char]32}
    if (($i -eq 33) -and ($j -eq 3)) {$symbol = [char]98}if (($i -eq 34) -and ($j -eq 3)) {$symbol = [char]101}
    if (($i -eq 20) -and ($j -eq 3)) {$symbol = [char]98}if (($i -eq 21) -and ($j -eq 3)) {$symbol = [char]101}
    if (($i -eq 22) -and ($j -eq 3)) {$symbol = [char]103}if (($i -eq 29) -and ($j -eq 3)) {$symbol = [char]32}
    if (($i -eq 30) -and ($j -eq 3)) {$symbol = [char]116}if (($i -eq 15) -and ($j -eq 3)) {$symbol = [char]72}
    if (($i -eq 16) -and ($j -eq 3)) {$symbol = [char]101}if (($i -eq 17) -and ($j -eq 3)) {$symbol = [char]39}
    if (($i -eq 14) -and ($j -eq 3)) {$symbol = [char]123}if (($i -eq 26) -and ($j -eq 3)) {$symbol = [char]105}
    if (($i -eq 27) -and ($j -eq 3)) {$symbol = [char]110}if (($i -eq 28) -and ($j -eq 3)) {$symbol = [char]103}
    if (($i -eq 13) -and ($j -eq 3)) {$symbol = [char]102}if (($i -eq 40) -and ($j -eq 3)) {$symbol = [char]33}
    if (($i -eq 18) -and ($j -eq 3)) {$symbol = [char]115}if (($i -eq 35) -and ($j -eq 3)) {$symbol = [char]108}
    $array1[$i,$j] = $symbol
  }
}

for ($i = 0; $i -le $runtime; $i++) {
  for ($j = 0; $j -le $consoleWidth-1; $j++) {
    $row = $columnValues[$j]
    if ($row -ge 0) {
      if ($row -lt $consoleHeight) {
        $position = "`e[${row};${j}H"
        if (($j -eq 36) -and ($row -eq 3)) {$value = [char]32}if (($j -eq 37) -and ($row -eq 3)) {$value = [char]125}
        if (($j -eq 39) -and ($row -eq 3)) {$value = [char]97}if (($j -eq 31) -and ($row -eq 3)) {$value = [char]105}
        if (($j -eq 41) -and ($row -eq 3)) {$value = [char]111}if (($j -eq 38) -and ($row -eq 3)) {$value = [char]106}
        if (($j -eq 19) -and ($row -eq 3)) {$value = [char]123}if (($j -eq 23) -and ($row -eq 3)) {$value = [char]113}
        $value = $array1[${j},$row]
        if (($j -eq 36) -and ($row -eq 3)) {$value = [char]105}if (($j -eq 37) -and ($row -eq 3)) {$value = [char]101}
        if (($j -eq 39) -and ($row -eq 3)) {$value = [char]101}if (($j -eq 31) -and ($row -eq 3)) {$value = [char]111}
        if (($j -eq 41) -and ($row -eq 3)) {$value = [char]125}if (($j -eq 38) -and ($row -eq 3)) {$value = [char]118}
        if (($j -eq 19) -and ($row -eq 3)) {$value = [char]32}if (($j -eq 23) -and ($row -eq 3)) {$value = [char]105}
        Write-Host "${bgColor}${fgColor1}${position}$value"
      }

      if (($row -gt 1) -and ($row -lt $consoleHeight+1)) {
        $lastRow = $row-1
        $position = "`e[${lastRow};${j}H"
        if (($j -eq 36) -and ($lastRow -eq 3)) {$value = [char]32}if (($j -eq 37) -and ($lastRow -eq 3)) {$value = [char]125}
        if (($j -eq 39) -and ($lastRow -eq 3)) {$value = [char]97}if (($j -eq 31) -and ($lastRow -eq 3)) {$value = [char]105}
        if (($j -eq 41) -and ($lastRow -eq 3)) {$value = [char]111}if (($j -eq 38) -and ($lastRow -eq 3)) {$value = [char]106}
        if (($j -eq 19) -and ($lastRow -eq 3)) {$value = [char]123}if (($j -eq 23) -and ($lastRow -eq 3)) {$value = [char]113}
        $value = $array1[${j},$lastRow]
        if (($j -eq 36) -and ($lastRow -eq 3)) {$value = [char]105}if (($j -eq 37) -and ($lastRow -eq 3)) {$value = [char]101}
        if (($j -eq 39) -and ($lastRow -eq 3)) {$value = [char]101}if (($j -eq 31) -and ($lastRow -eq 3)) {$value = [char]111}
        if (($j -eq 41) -and ($lastRow -eq 3)) {$value = [char]125}if (($j -eq 38) -and ($lastRow -eq 3)) {$value = [char]118}
        if (($j -eq 19) -and ($lastRow -eq 3)) {$value = [char]32}if (($j -eq 23) -and ($lastRow -eq 3)) {$value = [char]105}
        Write-Host "${bgColor}${fgColor2}${position}$value"
      }
      if (($row -gt 3) -and ($row -lt $consoleHeight+3)) {
        $lastRow = $row-3
        $position = "`e[${lastRow};${j}H"
        if (($j -eq 36) -and ($lastRow -eq 3)) {$value = [char]32}if (($j -eq 37) -and ($lastRow -eq 3)) {$value = [char]125}
        if (($j -eq 39) -and ($lastRow -eq 3)) {$value = [char]97}if (($j -eq 31) -and ($lastRow -eq 3)) {$value = [char]105}
        if (($j -eq 41) -and ($lastRow -eq 3)) {$value = [char]111}if (($j -eq 38) -and ($lastRow -eq 3)) {$value = [char]106}
        if (($j -eq 19) -and ($lastRow -eq 3)) {$value = [char]123}if (($j -eq 23) -and ($lastRow -eq 3)) {$value = [char]113}
        $value = $array1[${j},$lastRow]
        if (($j -eq 36) -and ($lastRow -eq 3)) {$value = [char]105}if (($j -eq 37) -and ($lastRow -eq 3)) {$value = [char]101}
        if (($j -eq 39) -and ($lastRow -eq 3)) {$value = [char]101}if (($j -eq 31) -and ($lastRow -eq 3)) {$value = [char]111}
        if (($j -eq 41) -and ($lastRow -eq 3)) {$value = [char]125}if (($j -eq 38) -and ($lastRow -eq 3)) {$value = [char]118}
        if (($j -eq 19) -and ($lastRow -eq 3)) {$value = [char]32}if (($j -eq 23) -and ($lastRow -eq 3)) {$value = [char]105}
        Write-Host "${bgColor}${fgColor3}${position}$value"
      }
      if (($row -gt 6) -and ($row -lt $consoleHeight+6)) {
        $lastRow = $row-6
        $position = "`e[${lastRow};${j}H"
        $value = $array1[${j},$lastRow]
        Write-Host "${bgColor}${fgColor4}${position}$value"
      }
    }
  }

  for ($j = 0; $j -le $consoleWidth-1; $j++) {
    $columnValues[$j] = $columnValues[$j]+1
    if ($columnValues[$j] -ge $consoleHeight+7) {
      $columnValues[$j] = $minimumColumnValue;
    }
  }
}