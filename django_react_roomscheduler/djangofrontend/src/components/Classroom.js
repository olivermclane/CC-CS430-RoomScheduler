import React from "react";
import "bootstrap/dist/css/bootstrap.min.css"

function Classroom({classroom, selectClassroom}){
    return (
        <div className='classroom card col-sm-3 m-1 text-center' onClick={() => {selectClassroom(classroom)}}>
            <div className='card-body'>
                Classroom number: {classroom.classroom_number}
                <br />
                Classroom total seats: {classroom.total_seats}
            </div>
        </div>
    )
}

export default Classroom