	<?php
		$sider = array("Hjem", "OmOss", "Reiserute", "Utstyr", "Turlogg", "Reisebrev", "Galleri", "Gjestebok", "Sponsorer");
		foreach($sider as $mv){
			if($mv == $side){
				$stil = "../../images/menylinje/" . $mv . "Rollover.jpg";
			}else{
				$stil = "../../images/menylinje/" . $mv . ".jpg";
			}
			?><a href="../../index.php?side=<?php echo $mv ?>" onmouseout="MM_swapImgRestore()"
			onmouseover="MM_swapImage('<?php echo $mv ?>','','../../images/menylinje/<?php echo $mv ?>Rollover.jpg',1)">
			<img src="<?php echo $stil ?>" alt="<?php echo $mv ?>" name="<?php echo $mv ?>" border="0"></a>
			<?php
		}
	?>