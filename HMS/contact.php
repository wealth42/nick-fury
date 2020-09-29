<!DOCTYPE html>
<html lang="en">
<head>
	<title>Contact</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="styles/contact.css">
	<link rel="stylesheet" type="text/css" href="styles/contact_responsive.css">
	<link rel="stylesheet" type="text/css" href="styles/bootstrap4/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="styles/main_styles.css">
	<link rel="stylesheet" type="text/css" href="styles/style.css">
	<link rel="stylesheet" type="text/css" href="styles/icon-font.min.css">
	<link rel="stylesheet" type="text/css" href="styles/main2.css">

</head>

<body>
		<div class="super_container">
		<div class="home">
			<div class="parallax_background parallax-window" style="opacity:0.5;" data-parallax="scroll"  data-image-src="images/box_3.jpg"></div>
			<header class="header" id="header">
				<div>
					<div class="header_top">
						<div class="container"/>
					</div>
				</div>			
				<section class="navigation">
					<div class="nav-container">
						<div class="brand">
							<a href="index.php">HMS</a>
						</div>
						<nav>
						<div class="nav-mobile">
								<a id="nav-toggle" href="#"><span></span></a>
							</div>
							
							<ul class="nav-list">
								<li><a href="index.php">Home</a></li>
								<li><a href="about.php">About</a></li>
								<li><a href="contact.php">Contact</a></li>
								<li><a href="#">User Login</a>
										<ul class="nav-dropdown">
										<li><a href="login/doctor/index.php">Doctor's Login</a></li>
										<li><a href="login/patient/index.php">Patient's Login</a></li>
										<li><a href="login/admin/index.php">Admin Login</a></li>
									</ul>
								</li>
								<li><a href="#">Sign-Up</a>
									<ul class="nav-dropdown">
										<li><a href="Signup/doctorsignup/signupdoctor.php">As a Doctor</a></li>
										<li><a href="Signup/patientsignup/signuppateint.php">As a Patient</a></li>
									</ul>
								</li>
							</ul>
						</nav>
					</div>
				</section>
			</header>
		</div>
	</div>	

	<div class="home_container">
		<div class="container">
			<div class="row">
				<div class="col">
					<div class="home_content">
						<div class="home_title">Contact us</div>
					</div>
				</div>
			</div>
		</div>
	</div>
<hr>

	<div class="container-contact100">
		<div class="wrap-contact100">
			<form action="action.php" method="post" class="contact100-form validate-form">
				<span class="contact100-form-title">Send Us A Message</span>
				<label class="label-input100" for="name">Tell us your name </label>

				<div class="wrap-input100 validate-input" data-validate = "Type full name">
					<input id="name" class="input100" type="text" name="name" placeholder=" Type your full name ">
					<span class="focus-input100"></span>
				</div>

				<label class="label-input100" for="email">Enter your email </label>
				<div class="wrap-input100 validate-input" data-validate = "Valid email is required: abc@mail.com" required>
					<input id="email" class="input100" type="text" name="email" placeholder="Eg. abc@mail.com">
		          <span class="focus-input100"></span>
				</div>

				<label class="label-input100" for="phone">Enter phone number</label>
				<div class="wrap-input100">
					<input id="phone" class="input100" type="text" name="phone" placeholder="Eg. +91 989 289 9997">
					<span class="focus-input100"></span>
				</div>
				




				<label class="label-input100" for="message">Message</label>
				<div class="wrap-input100 validate-input" data-validate = "Message is required">
					<textarea id="message" class="input100" name="message" placeholder="Write us a message"></textarea>
					<span class="focus-input100"></span>
				</div>

				<div class="container-contact100-form-btn">
			<input type="submit" value="Send Message" class="contact100-form-btn">
				</div>
			</form>

			<div class="contact100-more flex-col-c-m" style="background-image: url('images/bg-01.jpg');">
				<div class="flex-w size1 p-b-47">
					<div class="txt1 p-r-25">
						<span class="lnr lnr-map-marker"></span>
					</div>

					<div class="flex-col size2">
						<span class="txt1 p-b-20">Address</span>

						<span class="txt2">New Charni Road,Hinduja Lane,400004</span>
					
					</div>
				</div>

				<div class="dis-flex size1 p-b-47">
					<div class="txt1 p-r-25">
						<span class="lnr lnr-phone-handset"></span>
					</div>

					<div class="flex-col size2">
						<span class="txt1 p-b-20">Lets Talk</span>
						<span class="txt3">7045053487</span>
					</div>

				</div>

				<div class="dis-flex size1 p-b-47">
					<div class="txt1 p-r-25">
						<span class="lnr lnr-envelope"></span>
					</div>

					<div class="flex-col size2">
						<span class="txt1 p-b-20">General Support</span>
						<span class="txt3">akramulali8067@gmail.com
						</span>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div id="dropDownSelect1"></div>

	<script>
		$(".selection-2").select2({
			minimumResultsForSearch: 20,
			dropdownParent: $('#dropDownSelect1')
		});
	</script>
	<script async src="https://www.googletagmanager.com/gtag/js?id=UA-23581568-13"></script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'UA-23581568-13');
	</script>
<hr>

<!-- Footer -->

	<!-- Footer -->

	<footer class="footer">
		<div class="parallax_background parallax-window" data-parallax="scroll" data-image-src="images/footer.jpg" data-speed="0.8"></div>
		<div class="footer_content">
			<div class="container">
				<div class="row">
					<!-- About -->
					<div class="col-lg-3 footer_col">
						<div class="footer_about">
							<div class="HMS">
								<a href="#">HMS</a>	
							</div>
							<div class="footer_about_text">HOSPITAL MANAGEMENT SYSTEM</div>
								<div class="copyright">
								Copyright &copy; 2020
								All rights reserved | This project is made by Akramul and Malav</a>
							</div>
						</div>
					</div>
					<!-- Footer Contact -->
					<div class="col-lg-5 footer_col">
						<div class="footer_contact">
							<div class="footer_contact_title">Quick Contact</div>
							<div class="footer_contact_form_container">
								<form action="quickaction.php" method="post" class="footer_contact_form" id="footer_contact_form">
									<div class="d-flex flex-xl-row flex-column align-items-center justify-content-between">
										<input type="text" class="footer_contact_input" placeholder="Name"name="name" required="required">
										<input type="email" class="footer_contact_input" placeholder="E-mail" name="email" required="required">
									</div>
									<textarea class="footer_contact_input footer_contact_textarea" placeholder="Message" name="textarea" required="required"></textarea>
									<button class="footer_contact_button">send message</button>
								</form>
							</div>
						</div>
					</div>

					<!-- Footer Hours -->
					<div class="col-lg-4 footer_col">
						<div class="footer_hours">
							<div class="footer_hours_title">Opening Hours</div>
							<ul class="hours_list">
								<li class="d-flex flex-row align-items-center justify-content-start">
									<div>Monday – Thursday</div>
									<div class="ml-auto">8.00 – 19.00</div>
								</li>
								<li class="d-flex flex-row align-items-center justify-content-start">
									<div>Friday</div>
									<div class="ml-auto">8.00 - 18.30</div>
								</li>
								<li class="d-flex flex-row align-items-center justify-content-start">
									<div>Saturday</div>
									<div class="ml-auto">9.30 – 17.00</div>
								</li>
								<li class="d-flex flex-row align-items-center justify-content-start">
									<div>Sunday</div>
									<div class="ml-auto">9.30 – 15.00</div>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</footer>
<script src="js/jquery-3.3.1.min.js"></script>
<script src="styles/bootstrap4/bootstrap.min.js"></script>
<script src="plugins/easing/easing.js"></script>
<script src="plugins/parallax-js-master/parallax.min.js"></script>
<script src="js/custom.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&key=AIzaSyCIwF204lFZg1y4kPSIhKaHEXMLYxxuMhA"></script>
</body>
</html>