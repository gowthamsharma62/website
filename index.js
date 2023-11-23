    function isPalindrome(str) {
        str = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

        const reversedStr = str.split('').reverse().join('');

        return str === reversedStr;
    }

    const inputString = "A man, a plan, a canal: Panama";
    console.log(isPalindrome(inputString)); // Output: true