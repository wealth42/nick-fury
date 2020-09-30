<?php
	session_start();
	error_reporting(0);
	include('include/config.php');
	include('include/checklogin.php');
	check_login();
	function fill_floor($con)  
	{ 
     $output = '';  
     $sql = "SELECT * FROM floor";  
     $result = mysqli_query($con, $sql);  
     while($row = mysqli_fetch_array($result))  
    	{  
    	  $output .= '<option value="'.$row["floor_id"].'">'.$row["name"].'</option>';  
    	}  
    	return $output;  
 	}
 	function fill_rooms($con)  
 	{  
      $output = '';  
      $sql = "SELECT * FROM rooms";  
      $result = mysqli_query($con, $sql);  
      while($row = mysqli_fetch_array($result))  
      {  
    	$output .= '<div class="big-box">';  
    	$output .= '<div class="outer-box">'.$row["room_name"].'<br>Bed Available : '.$row["bed_available"];  
		$output .= '<br><br><button type="button" data-toggle="modal" data-target="#myModal1" class="btn btn-transparent btn-xs" tooltip="Edit"><i class="fa fa-pencil"></i></button>';
		$output .= '</div>';  
    	$output .= '</div>';  
      }  
  	  return $output;  
 	} 
	if(isset($_POST['submit']))
	{
		$name=$_POST['name'];
		$sql=mysqli_query($con,"insert into floor(name) values('$name')");
		if($sql)
		{
			echo "<script>alert('Floor added Successfully');</script>";
			echo "<script>window.location.href ='add-ward.php'</script>";
		}
	}
	if(isset($_POST['submit1']))
	{
		$room_name=$_POST['room_name'];
		$floor_id=$_POST['floor_id'];
		$bed_available=$_POST['bed_available'];
		$sql=mysqli_query($con,"insert into rooms(room_name,bed_available,floor_id) values('$room_name','$bed_available','$floor_id')");
		if($sql)
		{
			echo "<script>alert('Room added Successfully');</script>";
			echo "<script>window.location.href ='add-ward.php'</script>";
		}
	}
	if(isset($_POST['submit2']))
	{
		$bed_available=$_POST['bed_available'];
		$room_name=$_POST['room_name'];
		$sql=mysqli_query($con,"update rooms SET bed_available=$bed_available where room_name='$room_name'");
		if($sql)
		{
			echo "<script>alert('Bed Updated Successfully');</script>";
			echo "<script>window.location.href ='add-ward.php'</script>";
		}
	}
?>

<!DOCTYPE html>
<html>
<head>
	<title>Admin  | Manage Ward </title>
	<link rel="stylesheet" href="vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
	<link rel="stylesheet" href="vendor/themify-icons/themify-icons.min.css">
	<link rel="stylesheet" href="assets/css/styles.css">
	<link rel="stylesheet" href="assets/css/plugins.css">
	<link rel="stylesheet" href="assets/css/themes/theme-1.css" id="skin_color" />
	<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic"  type="text/css" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
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
					</ul>	
				</nav>
			</div>
		</div>	
		<div class="app-content">
			<?php error_reporting(0);?>
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
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-right">
						<li  style="padding-top:2%;font-family:Numans;">
							<h2>Hospital Management System</h2>
						</li>
						<li class="dropdown current-user">
							<a href class="dropdown-toggle" data-toggle="dropdown">
								<img src="assets/images/admin.png" > <span class="username">Admin<i class="ti-angle-down"></i></span>
							</a>
							<ul class="dropdown-menu dropdown-dark">	
								<li>
									<a href="change-password.php">Change Password</a>
								</li>
								<li>
									<a href="logout.php">Log Out</a>
								</li>
							</ul>
						</li>		
					</ul>
					<div class="close-handle visible-xs-block menu-toggler" data-toggle="collapse" href=".navbar-collapse">
						<div class="arrow-left"></div>
						<div class="arrow-right"></div>
					</div>
				</div>
			</header>
			<div class="main-content container" >
				<div class="wrap-content container">
					<!-- start: PAGE TITLE -->
					<section id="page-title">					
						<div class="col-sm-8">
							<h1 style="color: black;" class="mainTitle">Ward setup </h1>
						</div>
					</section>
					<div class="container">
						<div class="row">
							<div class="col-md-3"><br>
								<center> Floor List <br>	<br>
									<select name="floor" id="floor" style="width:150px;">
										<option value="" >Select </option>
										<?php echo fill_floor($con); ?>
									</select><br><br><br>
									<button type="button" class="btn btn-o btn-primary" data-toggle="modal" data-target="#myModal"> Add New Floor</button>
								</center>
								<div id="myModal" class="modal fade" role="dialog">
									<form role="form" method="POST"> 
										<div class="modal-dialog">
											<div class="modal-content">
												<div class="modal-header">
													<button type="button" class="close" data-dismiss="modal">&times;</button>
													<h4 class="modal-title"><center> New Floor</center></h4>
												</div>
												<div class="modal-body"><p>
													<div class="form-group">
														<label for="room type">Floor Ward Name </label>					
														<input type="text" name="name" class="form-control"  placeholder="Enter Floor ward name" required />
													</div></p><p>
													<div class="form-group">
														<label for="room availability">How many rooms ? </label>					
														<input type="text" name="" class="form-control"  placeholder="Enter number of rooms " required />
													</div></p>
												</div>
												<div class="modal-footer">
													<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
													<button type="submit" name="submit" id="submit" class="btn btn-default">Add</button>
												</div>
											</div>
										</div>
									</form>
								</div>
								<div id="myModal1" class="modal fade" role="dialog">
									<form role="form" method="POST"> 
										<div class="modal-dialog">
											<div class="modal-content">
												<div class="modal-header">
													<button type="button" class="close" data-dismiss="modal">&times;</button>
													<h4 class="modal-title"><center> Update Beds available  </center></h4>
												</div>
												<div class="modal-body"><p>
													<div class="form-group">
														<label for="room type">How many Beds available ?  </label>					
														<input type="text" name="bed_available" class="form-control"  placeholder="Enter number of beds available" required />
													</div></p><p>
													<div class="form-group">
														<label for="room availability">Room name  </label>					
														<input type="text" name="room_name" class="form-control"  placeholder="Enter room name " required />
													</div></p>
												</div>
												<div class="modal-footer">
													<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
													<button type="submit2" name="submit2" id="submit2" class="btn btn-default">Update</button>
												</div>
											</div>
										</div>
									</form>
								</div>
							</div>
							<div class="col-md-9"><br>
								<center> Ward Floor Rooms </center>
								<div class="big-box">
									<div class="row" id="show_room">  							
											<?php echo fill_rooms($con);?>
											  
									</div>	<br>
								</div>	<br> <br>
								<center>
									<button type="button" class="btn btn-o btn-primary" data-toggle="modal" data-target="#myModal1"> Add New Room</button>
								</center>
								<div id="myModal1" class="modal fade" role="dialog">
									<form role="form" method="POST"> 
										<div class="modal-dialog">
											<div class="modal-content">
												<div class="modal-header">
													<button type="button" class="close" data-dismiss="modal">&times;</button>
													<h4 class="modal-title"><center> New Room</center></h4>
												</div>
												<div class="modal-body">
													<div class="form-group">
														<label for="room type">Room name </label>					
														<input type="text" name="room_name" class="form-control"  placeholder="Enter Floor room name" required />
													</div>
													<div class="form-group">
														<label for="room availability">How many beds ? </label>					
														<input type="text" name="bed_available" class="form-control"  placeholder="Enter number of beds " required />
													</div>
													<div class="form-group">
														<label for="room availability">Which floor ? </label>					
														<input type="text" name="floor_id" class="form-control"  placeholder="Enter floor number " required />
													</div>
												</div>
												<div class="modal-footer">
													<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
													<button type="submit" name="submit1" id="submit1" class="btn btn-default">Add</button>
												</div>
											</div>
										</div>
									</form>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div><hr>	
	</div>
	<!-- start: MAIN JAVASCRIPTS -->
	<script src="vendor/jquery/jquery.min.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
	<script src="vendor/jquery-cookie/jquery.cookie.js"></script>
	
	<script src="assets/js/main.js"></script>
	<!-- start: JavaScript Event Handlers for this page -->
	<script src="assets/js/form-elements.js"></script>
	<script>  
		$(document).ready(
			function()
			{  
      			$('#floor').change(
					function()
					{  
           				var floor_id = $(this).val();  
           				$.ajax(
						{  
                			url:"load_data.php",  
							method:"POST",  
            				data:{floor_id:floor_id},  
							success:function(data)
							{  
                     			$('#show_room').html(data);  
                			}  
           				});  
    				});  
			}
		);  
 		jQuery(document).ready(
			function()
			{
				Main.init();
				FormElements.init();
			}
		);
	</script> 
</body>
</html>