<?php
session_start();
error_reporting(0);
include('include/config.php');
include('include/checklogin.php');
check_login();


if(isset($_POST['submit']))
{	$docspecialization=$_POST['Doctorspecialization'];
$docname=$_POST['docname'];
$docaddress=$_POST['clinicaddress'];
$docfees=$_POST['docfees'];
$doccontactno=$_POST['doccontact'];
$docemail=$_POST['docemail'];
$password=md5($_POST['npass']);
$sql=mysqli_query($con,"insert into doctors(specilization,doctorName,address,docFees,contactno,docEmail,password) values('$docspecialization','$docname','$docaddress','$docfees','$doccontactno','$docemail','$password')");
if($sql)
{
echo "<script>alert('Doctor info added Successfully');</script>";
echo "<script>window.location.href ='manage-doctors.php'</script>";

}
}
?>



<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Admin | Add Doctor</title>
		<link href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css" />
		<link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
		<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
		<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
		<link rel="stylesheet" href="assets/css/styles.css">
		<link rel="stylesheet" href="assets/css/plugins.css">
		<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />
 
 <script type="text/javascript">
function valid()
{
 if(document.adddoc.npass.value!= document.adddoc.cfpass.value)
{
alert("Password and Confirm Password Field do not match  !!");
document.adddoc.cfpass.focus();
return false;
}
return true;
}
</script>


<script>
function checkemailAvailability() {
$("#loaderIcon").show();
jQuery.ajax({
url: "check_availability.php",
data:'emailid='+$("#docemail").val(),
type: "POST",
success:function(data){
$("#email-availability-status").html(data);
$("#loaderIcon").hide();
},
error:function (){}
});
}
</script>


	</head>
	<body>
<div id="app">
			<div class="sidebar app-aside" id="sidebar">
				<div class="sidebar-container perfect-scrollbar">

<nav>
						
						<!-- start: MAIN NAVIGATION MENU -->
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
								<a href="javascript:void(0)">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-user"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Doctors </span><i class="icon-arrow"></i>
										</div>
									</div>
								</a>
								<ul class="sub-menu">
									<li>
										<a href="doctor-specilization.php">
											<span class="title"> Doctor Specialization </span>
										</a>
									</li>
									<li>
										<a href="add-doctor.php">
											<span class="title"> Add Doctor</span>
										</a>
									</li>
									<li>
										<a href="Manage-doctors.php">
											<span class="title"> Manage Doctors </span>
										</a>
									</li>
									
								</ul>
								</li>

								<li>
								<a href="javascript:void(0)">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-wheelchair"></i>
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
											<span class="title"> Manage Patients </span>
										</a>
									</li>
									
								</ul>
								</li>	
								<li>
								<a href="javascript:void(0)">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-layout"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Ward </span><i class="icon-arrow"></i>
										</div>
									</div>
								</a>
								<ul class="sub-menu">
									
									<li>
										<a href="add-ward.php">
											<span class="title"> Manage Ward </span>
										</a>
									</li>
									<li>
										<a href="room-setup.php">
											<span class="title"> Room type setup </span>
										</a>
									</li>
									
								</ul>
							</li>


								<li>
								<a href="patient-search.php">
									<div class="item-content">
										<div class="item-media">
											<i class="ti-search"></i>
										</div>
										<div class="item-inner">
											<span class="title"> Patient Search </span>
										</div>
									</div>
								</a>
							</li>
								</li>





						</ul>
						<!-- end: CORE FEATURES -->

						
					</nav>
					</div>
			</div>
<div class="app-content"><?php error_reporting(0);?>
<header class="navbar navbar-default navbar-static-top">
					<!-- start: NAVBAR HEADER -->
					<div class="navbar-header">
						<a href="#" class="sidebar-mobile-toggler pull-left hidden-md hidden-lg" class="btn btn-navbar sidebar-toggle" data-toggle-class="app-slide-off" data-toggle-target="#app" data-toggle-click-outside="#sidebar">
							<i class="ti-align-justify"></i>
						</a>
						
						<a class="navbar-brand" href="#">
							<h2 style="padding-top:20%;font-family:Numans;">HMS</h2>
						</a>
						
						
						<a href="#" class="sidebar-toggler pull-right visible-md visible-lg" data-toggle-class="app-sidebar-closed" data-toggle-target="#app">
							<i class="ti-align-justify"></i>
						</a>
						<a class="pull-right menu-toggler visible-xs-block" id="menu-toggler" data-toggle="collapse" href=".navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<i class="ti-view-grid"></i>
						</a>
					</div>
					<!-- end: NAVBAR HEADER -->
					<!-- start: NAVBAR COLLAPSE -->
					<div class="navbar-collapse collapse">
						<ul class="nav navbar-right">
		
							<!-- start: MESSAGES DROPDOWN -->
								<li  style="padding-top:2%;font-family:Numans;">
								<h2>Hospital Management System</h2>
							</li>
						
						
							<li class="dropdown current-user">
								<a href class="dropdown-toggle" data-toggle="dropdown">
									<img src="assets/images/system-administrator-png-system-administrator-logo-system-administrator-png-260_260.jpg"> <span class="username">Admin<i class="ti-angle-down"></i></i></span>
								</a>
								
								<ul class="dropdown-menu dropdown-dark">
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
							<!-- end: USER OPTIONS DROPDOWN -->
						</ul>



						<!-- start: MENU TOGGLER FOR MOBILE DEVICES -->
						<div class="close-handle visible-xs-block menu-toggler" data-toggle="collapse" href=".navbar-collapse">
							<div class="arrow-left"></div>
							<div class="arrow-right"></div>
						</div>
						<!-- end: MENU TOGGLER FOR MOBILE DEVICES -->
					</div>
				
					


					<!-- end: NAVBAR COLLAPSE -->
				</header>



				<!-- end: TOP NAVBAR -->
				<div class="main-content" >
					<div class="wrap-content container" id="container">
						<!-- start: PAGE TITLE -->
						<section id="page-title">
							<div class="row">
								<div class="col-sm-8">
									<h1 class="mainTitle">Admin | Add Doctor</h1>
																	</div>
								</div>
						</section>


						<!-- end: PAGE TITLE -->
						


						<!-- start: BASIC EXAMPLE -->
						<div class="container-fluid container-fullw bg-white">
							<div class="row">
								<div class="col-md-12">
									
									<div class="row margin-top-30">
										<div class="col-lg-8 col-md-12">
											<div class="panel panel-white">
												<div class="panel-heading">
													<h5 class="panel-title">Add Doctor</h5>
												</div>
						
												<div class="panel-body">
									
													<form role="form" name="adddoc" method="post" onSubmit="return valid();">
														<div class="form-group">
															<label for="DoctorSpecialization">
																Doctor Specialization
															</label>


							<select name="Doctorspecialization" class="form-control" required="true">
																<option value="">Select Specialization</option>
<?php $ret=mysqli_query($con,"select * from doctorspecilization");
while($row=mysqli_fetch_array($ret))
{
?>		
<option value="<?php echo htmlentities($row['specilization']);?>">
<?php echo htmlentities($row['specilization']);?></option>
												
<?php } ?>
																
															</select>
														</div>




<div class="form-group">
	<label for="doctorname">Doctor Name</label>					
<input type="text" name="docname" class="form-control"  placeholder="Enter Doctor Name" required="true">
</div>


<div class="form-group">
<label for="address">Doctor Clinic Address</label>
<textarea name="clinicaddress" class="form-control"  placeholder="Enter Doctor Clinic Address" required="true">
</textarea>
</div>



<div class="form-group">
<label for="fess">Doctor Consultancy Fees</label>
<input type="text" name="docfees" class="form-control"  placeholder="Enter Doctor Consultancy Fees" required="true">
</div>
	

<div class="form-group">
<label for="fess">Doctor Contact no</label>
<input type="text" name="doccontact" class="form-control"  placeholder="Enter Doctor Contact no" required="true">
</div>


<div class="form-group"><label for="fess">Doctor Email</label>
<input type="email" id="docemail" name="docemail" class="form-control"  placeholder="Enter Doctor Email id" required="true" onBlur="checkemailAvailability()">
<span id="email-availability-status"></span>
</div>


<div class="form-group"><label for="exampleInputPassword1">Password</label>
<input type="password" name="npass" class="form-control"  placeholder="New Password" required="required">
</div>


														
<div class="form-group">
	<label for="exampleInputPassword2">Confirm Password</label>
	<input type="password" name="cfpass" class="form-control"  placeholder="Confirm Password" required="required">
</div>
														
														
<button type="submit" name="submit" id="submit" class="btn btn-o btn-primary">Submit</button>
</form>
</div>
</div>
</div>
</div>
</div>

</div>
</div>
</div>
</div>
		
</div>



<hr>
	
		</div>





	<script src="vendor/jquery/jquery.min.js"></script>
		<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
		<script src="vendor/jquery-cookie/jquery.cookie.js"></script>
		
		<script src="assets/js/main.js"></script>
		<!-- start: JavaScript Event Handlers for this page -->
		<script src="assets/js/form-elements.js"></script>
				<script>
			jQuery(document).ready(function() {
				Main.init();
				FormElements.init();
			});
		</script>
		<!-- end: JavaScript Event Handlers for this page -->
		<!-- end: CLIP-TWO JAVASCRIPTS -->
	</body>
</html>