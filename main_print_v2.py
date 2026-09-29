"""print() 활용 v2: 함수와 반복문으로 표 형태 출력"""


def print_header(title: str, width: int = 40) -> None:
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def print_table(rows: list[tuple[str, int, float]]) -> None:
    print(f"{'이름':<8}{'나이':>6}{'점수':>10}")
    print("-" * 40)
    for name, age, score in rows:
        print(f"{name:<8}{age:>6}{score:>10.1f}")
    print("-" * 40)
    avg = sum(r[2] for r in rows) / len(rows)
    print(f"{'평균':<8}{'':>6}{avg:>10.2f}")


def progress_bar(total: int = 10) -> None:
    import time
    for i in range(total + 1):
        bar = "#" * i + "." * (total - i)
        print(f"\r진행률: [{bar}] {i * 100 // total:3d}%", end="", flush=True)
        time.sleep(0.1)
    print()


if __name__ == "__main__":
    students = [("홍길동", 21, 95.5), ("김철수", 22, 88.0), ("이영희", 20, 91.3)]
    print_header("Python Print Demo v2")
    print_table(students)
    progress_bar()
    print("완료!")
