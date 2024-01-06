// contact Form
document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contactForm');
    const submitButton = document.getElementById('submitButton');

    submitButton.addEventListener('click', function () {
        // Disable the button to prevent multiple clicks
        submitButton.disabled = true;

        // Add your form validation logic here
        const isFormValid = contactForm.checkValidity();

        if (isFormValid) {
            // Trigger SweetAlert for successful form submission
            Swal.fire({
                title: 'Success!',
                text: 'Your form has been submitted successfully!',
                icon: 'success',
                confirmButtonText: 'OK'
            }).then(() => {
                // Submit the form programmatically after the SweetAlert is closed
                contactForm.submit();
            });
        } else {
            // Trigger SweetAlert for invalid form data
            Swal.fire({
                title: 'Error!',
                text: 'Please fill in all required fields.',
                icon: 'error',
                confirmButtonText: 'OK'
            }).then(() => {
                // Re-enable the button after the SweetAlert is closed
                submitButton.disabled = false;
            });
        }
    });
});


// OrderForm

// Add SweetAlert on form submission
document.getElementById('addressForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    
    // You can customize the SweetAlert options according to your needs
    Swal.fire({
        title: 'Success!',
        text: 'Address added successfully.',
        icon: 'success',
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'OK'
    }).then((result) => {
        if (result.isConfirmed) {
            // Proceed with the form submission
            document.getElementById('addressForm').submit();
        }
    });
});


