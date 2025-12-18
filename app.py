from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route('/hocsinh', methods=['POST'])
def hocsinh():
    try:
        data=request.get_json()
    except:
        return jsonify({
            "status":"error",
            "message":"Dữ liệu không hợp lệ."
        }),400
    
    if not data or 'students' not in data or not isinstance(data['students'], list):
        return jsonify({
            "status": "error",
            "message": "Dữ liệu không hợp lệ."
        }), 400

    ds=data['students']

    total_count=len(ds)
    lap=[]
    dungtuoi=[]

    seen=set()

    for sv in ds:
        s_id=sv.get('student_id')
        name=sv.get('name')
        age=sv.get('age')
        gender=sv.get('gender')

        if s_id is None:
            return jsonify({
                "status":"error",
                "message":f"Dữ liệu không hợp lệ. Sinh viên thiếu ID."
            }),400
        if name is None:
            return jsonify({
                "status":"error",
                "message":f"Dữ liệu không hợp lệ. Sinh viên thiếu Tên."
            }),400
        if age is None:
            return jsonify({
                "status":"error",
                "message":f"Dữ liệu không hợp lệ. Sinh viên thiếu Tuổi."
            }),400
        
        if not isinstance(age,int):
            return jsonify({
                 "status":"error",
                "message":f"Dữ liệu không hợp lệ. Tuổi phải là sô nguyên"
            }),400
        
        if s_id in seen:
            lap.append(sv)
        else:
            seen.add(s_id)
        
            if age<23:
                dungtuoi.append(sv)

    response={
        "status": "success",
            "message": "Danh sách đã được xử lý thành công.",
            "total_students": total_count,
            "duplicate_students": lap,
            "students_eligible_for_free_ticket": dungtuoi
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)