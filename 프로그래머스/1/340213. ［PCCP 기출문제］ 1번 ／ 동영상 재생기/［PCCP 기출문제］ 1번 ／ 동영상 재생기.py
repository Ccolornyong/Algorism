def solution(video_len, pos, op_start, op_end, commands):
    def toseconde(time):
        mm, ss = map(int, time.split(":"))
        result = ss + mm * 60
        return result
    def toform(time):
        ss = time%60
        mm = time//60
        return f"{mm:02}:{ss:02}"
    
    sec_video_len = toseconde(video_len)
    sec_pos = toseconde(pos)
    sec_op_start = toseconde(op_start)
    sec_op_end = toseconde(op_end)
    
    if sec_op_start <= sec_pos <= sec_op_end:
        sec_pos = sec_op_end
    
    for i in commands:
        if i == "next":
            sec_pos += 10
            if sec_op_start <= sec_pos <= sec_op_end:
                sec_pos = sec_op_end
            if sec_pos > sec_video_len - 10:
                sec_pos = sec_video_len
                
        else:
            sec_pos -= 10
            if sec_op_start <= sec_pos <= sec_op_end:
                sec_pos = sec_op_end
            if sec_pos > sec_video_len - 10:
                sec_pos = sec_video_len
        if sec_pos<0:
            sec_pos = 0
    
    return toform(sec_pos)