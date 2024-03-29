<?php
	$con = mysqli_connect("localhost","root","","asteroid");
	$asteroid = $_GET['asteroid'];
	$query = mysqli_query($con,"SELECT * FROM approach WHERE distance='$asteroid'");
	$row = mysqli_fetch_array($query);
?>
<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title>Nasa Space Apps Challenge 2019</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="style.css" media="all" />
	<style type="text/css">
		.col-md-4 p{
			font-size:13px;
			background-color:#ccc;
			padding:5px;
		}
		
	</style>
</head>
<body">
	<div class="header">
		<div class="container">
			<h2>Abacus Xtreme <a href="asteroid-list.php" style="float:right;color:#fff;font-size:20px; padding-top:5px;">Asteroid List</a></h2>
		</div>
	</div>
	<div class="container">
		<div class="row">

			<div class="col-md-8">
						<div class="row">
							<div class="col-md-5">
								<label for="">Asteroid Name: </label>
							</div>
							<div class="col-md-7">
								<p><?php echo $row['name']; ?></p>
							</div>
						</div>
						<div class="row">
							<div class="col-md-5">
								<label for="">Estimated Diameter:</label>
							</div>
							<div class="col-md-7">
								<p><?php echo $row['diameter']; ?></p>
							</div>
						</div>
						<div class="row">
							<div class="col-md-5">
								<label for="">Close Approach Date:</label>
							</div>
							<div class="col-md-7">
								<p><?php echo $row['date']; ?></p>
							</div>
						</div>
						<div class="row">
							<div class="col-md-5">
								<label for="">Time:</label>
							</div>
							<div class="col-md-7">
								<p><?php echo $row['time']; ?></p>
							</div>
						</div>
						<div class="row">
							<div class="col-md-5">
								<label for="">Velocity:</label>
							</div>
							<div class="col-md-7">
								<?php echo $row['velocity'];?>
							</div>
						</div>
						<div class="row">
							<div class="col-md-5">
								<label for="">Distance to Earth:</label>
							</div>
							<div class="col-md-7">
								<?php echo $row['distance'];?>
							</div>
						</div>
						<div class="row">
							<div class="col-md-5">
								<label for="">Density:</label>
							</div>
							<div class="col-md-7">
							<?php echo "1500kg/m^3 " ;?>
							</div>
						</div>
						<div class="row">
							<div class="col-md-12">
								<?php 
									$status = $row['report'];
									if($status == "This asteroid could be dangerous to planet Earth!"){
										echo "<label class='bg-danger' style='padding:5px;color:#fff;'>$status</label>";
									}
									else{
										echo "<label class='bg-success' style='padding:5px;color:#fff;'>$status</label>";
									}
									
								?>
								
							</div>
						</div>
						
						
		
						
				
			</div>
			<div class="col-md-12">
				<center>
					<iframe scrolling="no" src="http://www.rankinstudio.com/asteroids/Main.php?PostType=byName&ObjName=<?php echo $row['name']; ?>" style="width: 100%; height: 500px;">
					</iframe>
				</center>
			</div>
		</div>
		<!-----<div class="row">
			<div class="col-md-4">
				<a href=""><img src="images/asteroid.jpg" alt="" /></a>
			</div>
		</div>------>
		<div class="row">
							<div class="col-md-12">
								<button data-toggle="collapse" data-target="#demo" class="btn btn-info">Calculate Impact</button>
								
								<div class="row collapse" id="demo">
									<div class="col-md-4">
										<h3 class="text-center">ATMOSPHERIC ENTRY</h3>
										<p>The projectile begins to breakup at an altitude of 65500 meters = 215000 ft <br /> The projectile reaches the ground in a broken condition. <br /> The mass of projectile strikes the surface at velocity 8.74 km/s = 5.43 miles/s<br />
										The impact energy is 5.91 x 10^17 Joules = 1.41 x 10^2 MegaTons.<br />
										The broken projectile fragments strike the ground in an ellipse of dimension 1.21 km by 0.856 km</p>
									</div>
									<div class="col-md-4">
										<h3 class="text-center">Energy</h3>
										<p>Energy before atmospheric entry: 9.35 x 10^17 Joules = 2.23 x 10^2 MegaTons TNT <br /> The average interval between impacts of this size somewhere on Earth during the last 4 billion years is 5 x 10^4 years</p>
									</div>
									<div class="col-md-4">
										<h3 class="text-center">Global Damages</h3>
										<p>The Earth is not strongly disturbed by the impact and loses negligible mass.<br /> The impact does not make a noticeable change in the tilt of Earth's axis (< 5 hundredths of a degree).<br /> The impact does not shift the Earth's orbit noticeably.</p>
									</div>
									<div class="col-md-4">
										<h3 class="text-center">Crater Dimensions</h3>
										<p>Crater shape is normal in spite of atmospheric crushing; fragments are not significantly dispersed.
										<br />Transient Crater Diameter: 2.26 km ( = 1.4 miles )
										<br />Transient Crater Depth: 798 meters ( = 2620 feet )
										<br />Final Crater Diameter: 2.82 km ( = 1.75 miles )
										<br />Final Crater Depth: 601 meters ( = 1970 feet )
										<br />The crater formed is a simple crater.
										<br />The floor of the crater is underlain by a lens of broken rock debris (breccia) with a maximum thickness of 278 meters ( = 913 feet ).
										<br />At this impact velocity ( < 12 km/s), little shock melting of the target occurs.</p>
									</div>
									<div class="col-md-4">
										<h3 class="text-center">Thermal Radiation</h3>
										<p>At this impact velocity ( < 15 km/ s, little vaporization occurs; no fireball is created, therefore, there is no thermal radiation damage.
										</p>
									</div>
									<div class="col-md-4">
										<h3 class="text-center">Seismic Effects</h3>
										<p>The major seismic shaking will arrive approximately 18.7 minutes after impact. <br />
										Richter Scale Magnitude:  6 <br />
										Mercalli Scale Intensity at a distance of 5602 km:

										Nothing would be felt.  However, seismic equipment may still detect shaking.</p>
									</div>
									<div class="col-md-4">
										<h3 class="text-center">Airblast</h3>
										<p>The air blast will arrive approximately 4.72 hours after impact.
										<br />Peak Overpressure: 50.6 Pa = 0.000506 bars = 0.00719 psi
										<br />Max wind velocity: 0.119 m/s = 0.267 mph
										<br />Sound Intensity: 34 dB (Easily Heard)</p>
									</div>
									
								</div>
								<div align="right" style="margin-bottom:20px;">
								<a href="http://localhost/asteroid/" class="btn btn-info">Go Back</a>
							</div>
							</div>
							
							
						</div>
	</div>
	
	
	
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>