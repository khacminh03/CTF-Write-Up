import path from "path";

const preTask = (solution) => {
    if (typeof solution !== "string") {
        throw new Error("Solution must be a string");
    }
    if (solution.length > 512) {
        throw new Error("Solution must be less than 512 characters");
    }
    if (solution === "flag") {
        throw new Error("Your solution can't be 'flag'");
    }
    if (solution === "./flag") {
        throw new Error("Your solution can't be './flag'");
    }
};

export const task1 = (solution) => {
    preTask(solution);
    if (!solution.startsWith("/robot") || solution.endsWith("/flag")) {
        console.log("inside task 1: " + solution);
        throw new Error(
            "You cannot access the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
        );
    }
    console.log("outside task 1 " + solution);
    const solutionPath = path.join("/", solution);
    console.log("solutionPath: " + solutionPath);
    if (solutionPath === "/flag") {
        console.log("You did it!")
    }
    return solutionPath === "/flag";
};

export const task2 = (solution) => {
    preTask(solution);
    solution = solution.replaceAll("../", "");
    console.log("inside task 2 after replace: " + solution)
    if (solution === "/flag") {
        console.log("inside check condition task 2: " + solution);
        throw new Error(
            "You cannot ACCESS the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
        );
    }
    const solutionPath = path.join("/", solution);
    return solutionPath === "/flag";
};

export const task3 = (solution) => {
    preTask(solution);
    console.log("Out side task 3 prepare solution: " + solution);
    if (solution.includes("../") || solution === "/flag") {
        console.log("inside task 3: " + solution);
        throw new Error(
            "You CANNOT ACCESS the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
        );
    }
    const solutionPath = path.join("/", solution);
    console.log("solution path task 3: " + solutionPath);
    return solutionPath === "/flag";
};

export const tasks = [
    `if (!solution.startsWith("/robot") || solution.endsWith("/flag")) {
    throw new Error(
        "You cannot access the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
    );
}

const solutionPath = path.join("/", solution);
return solutionPath === "/flag";`,
    `solution = solution.replaceAll("../", "");
    if (solution === "/flag") {
        throw new Error(
            "You cannot ACCESS the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
        );
    }

    const solutionPath = path.join("/", solution);
    return solutionPath === "/flag";`,
    `if (solution.includes("../") || solution === "/flag") {
    throw new Error(
        "You CANNOT ACCESS the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
    );
}

const solutionPath = path.join("/", solution);
return solutionPath === "/flag";`,
];
