def solution(genres, plays):
    answer = []
    
    Gplay_count = {} #장르별 재생횟수 합산
    
    song_genre = {} # 장르에 속한 노래 리스트 

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in Gplay_count: #장르별 재생횟수 합산
            Gplay_count[genre] += play
        else:
            Gplay_count[genre] = play
        
        if genre not in song_genre: 
            song_genre[genre] = [(play, i)] 
        else:
            song_genre[genre].append((play, i))

       # 각 장르별로 노래를 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬
    for genre in song_genre:
        # 재생 횟수는 내림차순
        song_genre[genre].sort(key=lambda x: (-x[0], x[1]))

    # 장르별 총 재생 횟수를 기준으로 내림차순 정렬
    sorted_genres = sorted(Gplay_count.keys(), key=lambda g: Gplay_count[g], reverse=True)
        
      
    # 각 장르 선택
    for genre in sorted_genres:
        # 해당 장르에서 최대 두 곡 선택
        temp = [song[1] for song in song_genre[genre][:2]]
        for i in temp:
            answer.append(i)
    return answer