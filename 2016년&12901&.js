//์ ๋ต 1(๐ฉ refactor 220425) - codeisneverodd
function solution(a, b) {
  let count = 0;
  const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  for (let i = 1; i < a; i++) count += month[i];
  count += b;
  return day[(count + 4) % 7]; // ๊ธ์์ผ ๋ถํฐ 1์ผ ์ด๋ฏ๋ก
}

//์ ๋ต 2 - yongchanson
function solution(a, b) {
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];

  let sum = b;
  for (
    let i = 0;
    i < a - 1;
    i++ //ex)5์์ธ ๊ฒฝ์ฐ 1~4์๊น์ง ๋ํด์ค๋ค.
  )
    sum += month[i];

  return week[sum % 7]; //1์ผ์ด ๊ธ์์ผ์ด๋ฏ๋ก, 0์ด๋ฉด ๋ชฉ์์ผ์ด ์ถ๋ ฅ๋์ด์ผ ํ๋ค.
}

//์ ๋ต 3 - chaerin-dev
function solution(a, b) {
  let week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  let dateStr = "2016-" + a + "- " + b;
  let date = new Date(dateStr);
  return week[date.getDay()];
}

//์ ๋ต 4 - chaerin-dev
function solution(a, b) {
  let arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  // 1์ 1์ผ๋ถํฐ a์ b์ผ๊น์ง ๋ฉฐ์น  ์ฐจ์ด์ธ์ง ์ ์ฅํ  ๋ณ์
  let passedDays = 0;
  // a๋ฌ ์ ๊น์ง์ ๋ชจ๋  ๋ฌ์ ๋ํด ๊ฐ ๋ฌ์ ๋ ์ง ์ ๋ํด์ค
  for (let i = 1; i < a; i++) passedDays += arr[i];
  // b์ผ ๋ํด์ฃผ๊ณ  1์ 0์ผ์ด ์๋ 1์ 1์ผ๋ถํฐ ์์ํ๋ฏ๋ก 1 ๋นผ์ค
  passedDays += b - 1;
  return week[(5 + passedDays) % 7];
}

//์ ๋ต 5 - prove-ability
function solution(a, b) {
  var answer = "";
  // 2016๋ 1์ 1์ผ์ ๊ธ์์ผ์๋๋ค. 2016๋ a์ b์ผ์ ๋ฌด์จ ์์ผ์ผ๊น์?
  const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const daysOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  // 2016๋ 1์ 1์ผ์ ๊ธ์์ผ๋ก 4๋ฅผ ๋ํด์ค๋ค
  let totalDays = 4;
  // a ์ด์  ๋ชจ๋  ๋ฌ์ ์ผ ์๋ฅผ ๋ํ๋ค
  for (let i = 0, len = a - 1; i < len; i++) {
    totalDays += daysOfMonth[i];
  }
  // totalDays ์ ํด๋น ์ผ์ ๋ํด์ฃผ๊ณ  7๋ก ๋๋ ๋๋จธ์ง
  const dayIndex = (totalDays + b) % 7;
  return days[dayIndex];
}
