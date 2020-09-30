<?php
session_start();
error_reporting(0);
include('include/config.php');
include('include/checklogin.php');
check_login();
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Doctor | Manage Patients</title>
		
		<link href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css" />
			<link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
		<link rel="stylesheet" href="assets/css/styles.css">
		<link rel="stylesheet" href="assets/css/plugins.css">
		<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />

</head>
	<body>
	
		<div id="app">
		<div class="sidebar app-aside" id="sidebar">
				<div class="sidebar-container perfect-scrollbar">
					<nav>
					
						<div class="navbar-title">
							<span>Main Navigation</span>
						</div>
					
						<ul class="main-navigation-menu">
					
							<li>
								<a href="dashboard.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-home"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Dashboard </span>
										</div>
									</div>
								</a>
							</li>
							

							<li>
								<a href="appointment-history.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-list"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Appointment History </span>
										</div>
									</div>
								</a>
							</li>
					
							<li>
								<a href="javascript:void(0)">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-user"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Patients </span><i class="icon-arrow"></i>
										</div>
									</div>
								</a>
								<ul class="sub-menu">
									
									<li>
										<a href="add-patient.php">
											<span class="title"> Add Patient</span>
										</a>
									</li>
									<li>
										<a href="manage-patient.php">
											<span class="title"> Manage Patient </span>
										</a>
									</li>
									
								</ul>
								</li>




                             <li><a href="search.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-search"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Search </span>
										</div>
									</div>
								</a>
							</li>


						</ul>
						
					</nav>
					</div>
			</div>
<?php error_reporting(0);?>
<header class="navbar navbar-default navbar-static-top">
					<div class="navbar-header">

						<a href="#" class="sidebar-mobile-toggler pull-left hidden-md hidden-lg" class="btn btn-navbar sidebar-toggle" data-toggle-class="app-slide-off" data-toggle-target="#app" data-toggle-click-outside="#sidebar">
							<i class="ti-align-justify"></i>
						</a>

						<a class="navbar-brand" href="#">
							<h2 style="padding-top:20% ">HMS</h2>
						</a>
						
						<a href="#" class="sidebar-toggler pull-right visible-md visible-lg" data-toggle-class="
						app-sidebar-closed" data-toggle-target="#app">
							<i class="ti-align-justify"></i>
						</a>
						
						<a class="pull-right menu-toggler visible-xs-block" id="menu-toggler" data-toggle="collapse" href=".navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<i class="ti-view-grid"></i>
						</a>
					</div>
					
					<div class="navbar-collapse collapse">
						<ul class="nav navbar-right">
					
								<li  style="padding-top:2% ">
								<h2>Hospital Management System</h2>
							</li>
						
						
							
						
							<li class="dropdown current-user">
								<a href class="dropdown-toggle" data-toggle="dropdown">
									<img src="assets/images/doctor-icon-vector-11004500.jpg" > 
									<span class="username">
									<?php $query=mysqli_query($con,"select fullname from doctorsignup where id='".$_SESSION['id']."'"); 
                               while($row=mysqli_fetch_array($query))
                             {
                                 	echo $row['fullname'];
                              }
									?> 
									<i class="ti-angle-down"></i></i></span></a>

								<ul class="dropdown-menu dropdown-dark">
									
									<li>
										<a href="edit-profile.php">
											My Profile
										</a>
									</li>
								
									<li>
										<a href="change-password.php">
											Change Password
										</a>
									</li>
									
									<li>
										<a href="logout.php">
											Log Out
										</a>
									</li>
								</ul>
							</li>


								</ul>
					
						<div class="close-handle visible-xs-block menu-toggler" data-toggle="collapse" 
						href=".navbar-collapse">
							<div class="arrow-left"></div>
							<div class="arrow-right"></div>
						</div>
						
							</div>
				
						</header>


<div class="main-content" >
<div class="wrap-content container" id="container">
<section id="page-title">
<div class="row">
<div class="col-sm-8">
<h1 class="mainTitle">Doctor | Manage Patients</h1>
</div>
</div>
</section>

<div class="container-fluid container-fullw bg-white">
<div class="row">
<div class="col-md-12">
<h5 class="over-title margin-bottom-15"><span class="text-bold">Manage  Patients</span></h5>
<?php
                               $vid=$_GET['viewid'];
                               $ret=mysqli_query($con,"select * from tblpatient where ID='$vid'");
$cnt=1;
while ($row=mysqli_fetch_array($ret)) {
                               ?>
<table border="1" class="table table-bordered">
 <tr align="center">
<td colspan="4" style="font-size:20px;color:blue">
 Patient Details</td></tr>

    <tr>
	<br>
    <th scope>Patient Name</th>
    <td><?php  echo $row['PatientName'];?></td>
    <th scope>Patient Email</th>
    <td><?php  echo $row['PatientEmail'];?></td>
  </tr>
  <tr>
    <th scope>Patient Mobile Number</th>
    <td><?php  echo $row['PatientContno'];?></td>
    <th>Patient Address</th>
    <td><?php  echo $row['PatientAdd'];?></td>
  </tr>
    <tr>
    <th>Patient Gender</th>
    <td><?php  echo $row['PatientGender'];?></td>
    <th>Patient Age</th>
    <td><?php  echo $row['PatientAge'];?></td>
  </tr>
  <tr>
    
    <th>Patient Medical History ( if any )</th>
    <td><?php  echo $row['PatientMedhis'];?></td>
     <th>Patient Reg Date</th>
    <td><?php  echo $row['CreationDate'];?></td>
  </tr>
 
<?php }?>
</table>
                          
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
		<footer>
				<div class="footer-inner">
					<div class="pull-left">
						&copy; <span class="current-year"></span><span class="text-bold text-uppercase"> HMS</span>. <span>All rights reserved</span>
					</div>
					<div class="pull-right">
						<span class="go-top"><i class="ti-angle-up"></i></span>
					</div>
				</div>
			</footer>
				</div>
			</div>
		</div>
		<script src="css-and-js-file/jquery.min.js"></script>
		<script src="css-and-js-file/bootstrap.min.js"></script>
		<script src="css-and-js-file/jquery.cookie.js"></script>
		<script src="assets/js/main.js"></script>
		<script src="assets/js/form-elements.js"></script>
<script>
			jQuery(document).ready(function() {
				Main.init();
				FormElements.init();
			});
		</script>
	</body>
</html>
