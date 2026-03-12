$(document).ready(function() {
    let studentCounter = 1;
    
    $('#addStudent').click(function() {
        let newStudent = `
            <div class="student-card" id="student-${studentCounter}">
                <div class="student-header">  
                    <h3>Студент #${studentCounter + 1}</h3>
                    <button type="button" class="delete-btn" data-id="${studentCounter}">✖</button>
                </div>
                <input type="text" name="name_${studentCounter}" placeholder="Имя студента" required>
                <input type="number" name="age_${studentCounter}" placeholder="Возраст" required>
                <input type="email" name="email_${studentCounter}" placeholder="Email" required>
            </div>
        `;
        $('#students-container').append(newStudent);
        studentCounter++;
    });
    
    $(document).on('click', '.delete-btn', function() {
        $(this).closest('.student-card').remove();
    });
});