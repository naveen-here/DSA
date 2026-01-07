int dfs(TreeNode* root){
    if (!root) return 0;
    int sum=root->val+dfs(root->left)+dfs(root->right);
    ans=max(ans, (total-sum)*sum);
    return sum;
}