import os
import re
import glob

folder_path = './'
files = sorted(os.listdir(folder_path), key=len)

for filename in files:
    # 이미지 확장자들을 모두 포함한다.
    if filename.lower().endswith(('.gif', '.jpg', '.jpeg', '.png')):
        # 이미 변환이 완료된 파일(no숫자.확장자)은 건너뛴다. (중복 실행 방지)
        if re.match(r'^no\d+(_\d+)?\.', filename):
            continue
            
        # 파일 이름에서 숫자 추출
        match = re.search(r'\d+', filename)
        
        if match:
            num = match.group()
            ext = os.path.splitext(filename)[1].lower()
            
            # 해당 번호(예: no96)로 시작하는 파일이 폴더에 몇 개나 있는지 확인한다. (확장자 무관)
            existing_files = glob.glob(os.path.join(folder_path, f'no{num}.*')) + \
                             glob.glob(os.path.join(folder_path, f'no{num}_*.*'))
            
            count = len(existing_files)
            
            # 파일 개수에 따라 번호를 매긴다.
            if count == 0:
                final_name = f'no{num}{ext}'
            else:
                final_name = f'no{num}_{count + 1}{ext}'
                
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, final_name)
            
            # 이름 변경 실행
            if old_file != new_file:
                os.rename(old_file, new_file)
                print(f'변경 완료: {filename} -> {final_name}')