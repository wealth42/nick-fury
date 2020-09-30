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
		<title>Doctor | Search Patients</title>
		
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
					<!-- start: NAVBAR HEADER -->
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
<h1 class="mainTitle">Doctor | Search Patients</h1>
</div>
</div>
</section>

<div class="container-fluid container-fullw bg-white">
<div class="row">
<div class="col-md-12">
<form role="form" method="post" name="search">
<div class="form-group">
<label for="doctorname">Search by Name/Mobile No.</label>

<input type="text" name="searchdata" id="searchdata" class="form-control" value="" required='true'>
</div>

<button type="submit" name="search" id="submit" class="btn btn-o btn-primary">Search</button>
</form>	

<?php
if(isset($_POST['search']))
{ 
$sdata=$_POST['searchdata'];
?>

<h4 align="center">Result for "<?php echo $sdata;?>" keyword </h4>

<table class="table table-hover" id="sample-table-1">
<thead>

<tr>
<th class="center">src</th>
<th>Patient Name</th>
<th>Patient Contact Number</th>
<th>Patient Gender </th>
<th>Creation Date </th>

<th>Action</th>
</tr>

</thead>

<tbody>
<?php
$sql=mysqli_query($con,"select * from tblpatient where PatientName like '%$sdata%'|| PatientContno like '%$sdata%'");
$num=mysqli_num_rows($sql);
if($num>0){
$cnt=1;
while($row=mysqli_fetch_array($sql))
{
?>
<tr>
<td class="center"><?php echo $cnt;?>.</td>
<td class="hidden-xs"><?php echo $row['PatientName'];?></td>
<td><?php echo $row['PatientContno'];?></td>
<td><?php echo $row['PatientGender'];?></td>
<td><?php echo $row['CreationDate'];?></td>
</td>
<td>
<a href="view-patient.php?viewid=<?php echo $row['ID'];?>"><i class="fa fa-eye"></i></a>

</td>
</tr>
<?php 
$cnt=$cnt+1;
} 
}
else
{ 
?>

<tr>
    <td colspan="8"> No record found against this search</td>
</tr>
   
<?php }}
 ?>
</tbody>
</table>
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
		<script src="assets/js/form-elements.js"></script>
	<script>
			jQuery(document).ready(function() {
				Main.init();
				FormElements.init();
			});
		</script>
	</body>
</html>
