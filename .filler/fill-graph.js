const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// YOUR GitHub info
const authorName = "Saad Mir";
const authorEmail = "60347194+saadmir3163@users.noreply.github.com";

// Input
const startDateStr = "2020-01-01";
const endDateStr = "2025-3-19";
const maxCommitsPerDay = 4;
const skipChance = 0.25;

// Setup
const startDate = new Date(startDateStr);
const endDate = new Date(endDateStr);
const commitFile = path.resolve(__dirname, 'commit.txt');

// Ensure commit.txt exists
if (!fs.existsSync(commitFile)) {
    fs.writeFileSync(commitFile, '');
    execSync(`git add ${commitFile}`);
    execSync(`GIT_AUTHOR_DATE="${startDateStr}T12:00:00" GIT_COMMITTER_DATE="${startDateStr}T12:00:00" GIT_AUTHOR_NAME="${authorName}" GIT_AUTHOR_EMAIL="${authorEmail}" GIT_COMMITTER_NAME="${authorName}" GIT_COMMITTER_EMAIL="${authorEmail}" git commit -m "Initial backdated commit"`);
    execSync('git push');
    console.log("✅ Created initial commit.");
}

function isWeekend(date) {
    const d = date.getDay();
    return d === 0 || d === 6;
}

function addDays(date, days) {
    const copy = new Date(date);
    copy.setDate(copy.getDate() + days);
    return copy;
}

function formatDate(date, hour) {
    return date.toISOString().split('T')[0] + ` ${hour}:00:00`;
}

// Start filling
let currentDate = startDate;

while (currentDate <= endDate) {
    if (!isWeekend(currentDate) && Math.random() > skipChance) {
        const commitsToday = Math.floor(Math.random() * maxCommitsPerDay) + 1;

        for (let i = 0; i < commitsToday; i++) {
            const hour = 10 + i;
            const commitDate = formatDate(currentDate, hour);

            const env = `GIT_AUTHOR_DATE="${commitDate}" GIT_COMMITTER_DATE="${commitDate}" GIT_AUTHOR_NAME="${authorName}" GIT_AUTHOR_EMAIL="${authorEmail}" GIT_COMMITTER_NAME="${authorName}" GIT_COMMITTER_EMAIL="${authorEmail}"`;

            fs.appendFileSync(commitFile, `${commitDate}\n`);
            execSync(`git add ${commitFile}`);
            execSync(`${env} git commit -m "Backdated commit for ${commitDate}"`);
            console.log(`✅ Commit done on ${commitDate}`);
        }
    } else {
        console.log(`⏭️ Skipping ${currentDate.toISOString().split('T')[0]}`);
    }

    currentDate = addDays(currentDate, 1);
}

// Final push
execSync('git push');
console.log("🚀 All commits pushed successfully!");
