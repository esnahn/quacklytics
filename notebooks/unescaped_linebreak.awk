BEGIN {
    buf = ""        # 레코드 조립용 버퍼
    pipe_count = 0  # buf에 누적된 파이프 개수
}
{
    line = $0
    # remove any CR or LF characters in what awk saw as one record
    gsub(/[\r\n]$/, "", line)

    # split으로 파이프로 분리된 컬럼 수 계산
    this_count = split(line, arr, "|") - 1

    if (buf == "") {
        # 버퍼 없으면 새 레코드 시작
        buf = line
        pipe_count = this_count
    } else {
        # 아직 파이프가 부족했으면 다음 줄 이어붙이기
        # 공백으로 대체하여 연결
        buf = buf " " line
        pipe_count += this_count
    }

    if (pipe_count == EXPC) {
        # 기대치(EXPC)와 일치하면, 완성된 레코드 출력
        print buf
        buf = ""
        pipe_count = 0
    }
    else if (pipe_count > EXPC) {
        # 파이프 초과 시 경고 후 버퍼 초기화
        print "WARNING: pipe overflow in record:\n" buf > "/dev/stderr"
        buf = ""
        pipe_count = 0
    }
    # pipe_count < EXPC 이면, 아직 레코드가 미완성이므로 대기
}
END {
    # 남은 버퍼가 있으면 마지막 레코드로 출력
    if (buf != "") print buf
}