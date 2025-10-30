#!/usr/bin/env python3
"""
iOS 시뮬레이터 설정 및 실행 스크립트
"""

import subprocess
import sys
import time

def check_xcode_installed():
    """Xcode 설치 확인"""
    try:
        result = subprocess.run(['xcode-select', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Xcode Command Line Tools 설치됨")
            return True
        else:
            print("❌ Xcode Command Line Tools 미설치")
            return False
    except FileNotFoundError:
        print("❌ Xcode Command Line Tools 미설치")
        return False

def install_xcode_tools():
    """Xcode Command Line Tools 설치"""
    print("🔧 Xcode Command Line Tools 설치 중...")
    try:
        subprocess.run(['xcode-select', '--install'], check=True)
        print("✅ Xcode Command Line Tools 설치 시작됨")
        print("⏳ 설치 완료 후 다시 실행해주세요")
        return True
    except Exception as e:
        print(f"❌ Xcode Command Line Tools 설치 실패: {e}")
        return False

def get_available_simulators():
    """사용 가능한 iOS 시뮬레이터 목록 조회"""
    try:
        result = subprocess.run(['xcrun', 'simctl', 'list', 'devices', 'available'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return ""
    except Exception as e:
        print(f"❌ 시뮬레이터 목록 조회 실패: {e}")
        return ""

def list_simulators():
    """시뮬레이터 목록 출력"""
    print("\n📱 사용 가능한 iOS 시뮬레이터:")
    simulators = get_available_simulators()
    if simulators:
        lines = simulators.split('\n')
        current_ios = ""
        for line in lines:
            line = line.strip()
            if line.startswith('-- iOS'):
                current_ios = line
                print(f"\n{current_ios}")
            elif 'iPhone' in line or 'iPad' in line:
                if '(Booted)' in line:
                    print(f"  🟢 {line}")
                elif '(Shutdown)' in line:
                    print(f"  ⚪ {line}")
                else:
                    print(f"  📱 {line}")
    else:
        print("❌ 시뮬레이터를 찾을 수 없습니다")

def start_simulator(device_name="iPhone 15"):
    """iOS 시뮬레이터 시작"""
    print(f"\n🚀 iOS 시뮬레이터 '{device_name}' 시작 중...")
    
    try:
        # 1. 시뮬레이터 부팅
        print("1️⃣ 시뮬레이터 부팅 중...")
        boot_result = subprocess.run(['xcrun', 'simctl', 'boot', device_name], 
                                   capture_output=True, text=True)
        
        if boot_result.returncode == 0:
            print("✅ 시뮬레이터 부팅 성공")
        elif "Unable to boot device in current state: Booted" in boot_result.stderr:
            print("✅ 시뮬레이터가 이미 부팅되어 있습니다")
        else:
            print(f"❌ 시뮬레이터 부팅 실패: {boot_result.stderr}")
            return False
        
        # 2. 시뮬레이터 앱 열기
        print("2️⃣ 시뮬레이터 앱 열기...")
        subprocess.run(['open', '-a', 'Simulator'], check=True)
        print("✅ 시뮬레이터 앱 열기 성공")
        
        # 3. 시뮬레이터 준비 대기
        print("3️⃣ 시뮬레이터 준비 대기 중...")
        time.sleep(5)
        
        print(f"🎉 iOS 시뮬레이터 '{device_name}' 준비 완료!")
        return True
        
    except Exception as e:
        print(f"❌ 시뮬레이터 시작 실패: {e}")
        return False

def shutdown_all_simulators():
    """모든 시뮬레이터 종료"""
    print("\n🛑 모든 시뮬레이터 종료 중...")
    try:
        subprocess.run(['xcrun', 'simctl', 'shutdown', 'all'], check=True)
        print("✅ 모든 시뮬레이터 종료 완료")
        return True
    except Exception as e:
        print(f"❌ 시뮬레이터 종료 실패: {e}")
        return False

def main():
    """메인 함수"""
    print("🍎 iOS 시뮬레이터 설정 도구")
    print("=" * 40)
    
    # Xcode 설치 확인
    if not check_xcode_installed():
        print("\n❌ Xcode Command Line Tools가 설치되지 않았습니다")
        install_xcode_tools()
        return
    
    # 명령행 인수 처리
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "list":
            list_simulators()
        elif command == "start":
            device_name = sys.argv[2] if len(sys.argv) > 2 else "iPhone 15"
            start_simulator(device_name)
        elif command == "shutdown":
            shutdown_all_simulators()
        else:
            print_usage()
    else:
        # 기본 동작: 시뮬레이터 목록 표시 후 iPhone 15 시작
        list_simulators()
        
        print("\n" + "=" * 40)
        user_input = input("iPhone 15 시뮬레이터를 시작하시겠습니까? (y/n): ").lower()
        
        if user_input in ['y', 'yes', '']:
            start_simulator("iPhone 15")
        else:
            print("시뮬레이터 시작을 취소했습니다")

def print_usage():
    """사용법 출력"""
    print("\n📖 사용법:")
    print("python ios_setup.py                    # 시뮬레이터 목록 표시 후 iPhone 15 시작")
    print("python ios_setup.py list               # 시뮬레이터 목록만 표시")
    print("python ios_setup.py start              # iPhone 15 시뮬레이터 시작")
    print("python ios_setup.py start 'iPhone 14'  # 특정 시뮬레이터 시작")
    print("python ios_setup.py shutdown           # 모든 시뮬레이터 종료")

if __name__ == "__main__":
    main()