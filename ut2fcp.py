type="0"
origin_mvt_file_name="kick_origin.txt"
fcp_mvt_file_name="Kick_Motion.xml"
force_wait_time="0.02"

joint_index = [
    '14', '16', '18', '20',
    '2', '4', '6', '8', '10', '12',
    '3', '5', '7', '9', '11', '13',
    '15', '17', '19', '21',
    '22', '23'
]

with open(origin_mvt_file_name,'r') as origin_mvt:
    single_phases = origin_mvt.readlines()
    mvt_str = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<behavior description=\"Kick motion with right leg\" auto_head=\"1\">\n"
    for single_phase in single_phases:
        phase_joint_angles = single_phase.split()
        mvt_str += "    <slot delta=\"" + (str(float(phase_joint_angles[0]) / 1000) if force_wait_time==None else force_wait_time + "\">\n")
        joint_list_length=phase_joint_angles.__len__()
        if type!="4":
            joint_list_length-=2
        for i in range(3, joint_list_length):
            joint_angle = phase_joint_angles[i]
            joint_id = joint_index[i - 3]
            if joint_id == "20" or joint_id == "5" or joint_id == "13" or joint_id == "17":
                joint_angle = str(-float(joint_angle))
            mvt_str += "        <move id=\"" + joint_id + "\" angle=\"" + joint_angle + "\"/>\n"
        mvt_str += "    </slot>\n"
    mvt_str += "</behavior>\n"

with open(fcp_mvt_file_name,'a') as f:
    f.write(mvt_str)
