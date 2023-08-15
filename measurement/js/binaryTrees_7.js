/* The Computer Language Benchmarks Game
   https://salsa.debian.org/benchmarksgame-team/benchmarksgame/

   contributed by Léo Sarrazin
   multi thread by Andrey Filatkin
   sequential by Isaac Gouy
*/

function mainThread() {
    var maxDepth = Math.max(6, parseInt(process.argv[2]));

    var stretchDepth = maxDepth + 1;
    var check = itemCheck(bottomUpTree(stretchDepth));
    console.log("stretch tree of depth " + stretchDepth + "\t check: " + check);

    var longLivedTree = bottomUpTree(maxDepth);

    for (var depth = 4; depth <= maxDepth; depth += 2) {
        var iterations = 1 << maxDepth - depth + 4;
        work(iterations, depth);
    }

    console.log("long lived tree of depth " + maxDepth + "\t check: " + itemCheck(longLivedTree));
}

function work(iterations, depth) {
    var check = 0;
    for (var i = 0; i < iterations; i++) {
        check += itemCheck(bottomUpTree(depth));
    }
    console.log(iterations + "\t trees of depth " + depth + "\t check: " + check);
}

function TreeNode(left, right) {
    return { left: left, right: right };
}

function itemCheck(node) {
    if (node.left === null) {
        return 1;
    }
    return 1 + itemCheck(node.left) + itemCheck(node.right);
}

function bottomUpTree(depth) {
    return depth > 0
        ? new TreeNode(bottomUpTree(depth - 1), bottomUpTree(depth - 1))
        : new TreeNode(null, null);
}

mainThread();