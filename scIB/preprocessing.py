import numpy as np
from matplotlib import pyplot as plt
import sns
import scanpy as sc
from scIB.utils import *


def plot_scatter(adata, count_threshold=0, gene_threshold=0,
                 color='tissue', title='', lab_size=15, tick_size=11, legend_loc='right margin',
                palette=None):
    
    ax = sc.pl.scatter(adata, 'n_counts', 'n_genes', color=color, show=False,
                       legend_fontweight=50, legend_loc=legend_loc, palette=palette)
    ax.set_title(title, fontsize=lab_size)
    ax.set_xlabel("Count depth",fontsize=lab_size)
    ax.set_ylabel("Number of genes",fontsize=lab_size)
    ax.tick_params(labelsize=tick_size)
    
    if gene_threshold > 0:def plot_scatter(adata, count_threshold=0, gene_threshold=0,
                 color='tissue', title='', lab_size=15, tick_size=11, legend_loc='right margin',
                palette=None):
    
    ax = sc.pl.scatter(adata, 'n_counts', 'n_genes', color=color, show=False,
                       legend_fontweight=50, legend_loc=legend_loc, palette=palette)
    ax.set_title(title, fontsize=lab_size)
    ax.set_xlabel("Count depth",fontsize=lab_size)
    ax.set_ylabel("Number of genes",fontsize=lab_size)
    ax.tick_params(labelsize=tick_size)
    
    if gene_threshold > 0:
        ax.axhline(gene_threshold, 0,1, color='red')
    if count_threshold > 0:
        ax.axvline(count_threshold, 0,1, color='red')
    
    fig = plt.gcf()
    cbar_ax = fig.axes[-1]
    cbar_ax.tick_params(labelsize=tick_size)
    f1 = ax.get_figure()
    plt.show()
    
#Data quality summary plots        
def plot_count_filter(adata, obs_col='n_counts', bins=60, lower=0, upper=np.inf, filter_lower=0, filter_upper=np.inf):
    
    plot_data = adata.obs[obs_col]
    
    sns.distplot(plot_data, kde=False, bins=bins)
    
    if lower > 0:
        plt.axvline(lower, linestyle = '--', color = 'g')
    if filter_lower > 0:
        plt.axvline(filter_lower, linestyle = '-', color = 'r')
    if not np.isinf(upper):
        plt.axvline(upper, linestyle = '--', color = 'g')
    if not np.isinf(upper):
        plt.axvline(filter_upper, linestyle = '-', color = 'r')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
    plt.show()
    
    # determine lower bound of total, look at points below lower bound
    if filter_lower > 0:
        print(f"lower threshold: {filter_lower}")
        sns.distplot(plot_data[plot_data < lower], kde=False, bins=bins)
        plt.axvline(filter_lower, linestyle = '-', color = 'r')
        plt.axvline(lower, linestyle = '--', color = 'g')
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
        plt.show()

    # determine upper bound of total
    if not np.isinf(filter_upper) and not np.isinf(upper):
        print(f"upper threshold: {filter_upper}")
        sns.distplot(plot_data[plot_data > upper], kde=False, bins=bins)
        plt.axvline(filter_upper, linestyle = '-', color = 'r')
        plt.axvline(upper, linestyle = '--', color = 'g')
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
        plt.show()
        
def plot_QC(adata, color=None, bins=60, legend_loc='right margin', histogram=True,
            gene_threshold=(0,np.inf), 
            gene_filter_threshold=(0,np.inf),
            count_threshold=(0,np.inf), 
            count_filter_threshold=(0,np.inf)):
    
    if count_filter_threshold == (0, np.inf):
        count_filter_threshold = count_threshold
    if gene_filter_threshold == (0, np.inf):
        gene_filter_threshold = gene_threshold
    
    # 2D scatter plot
    plot_scatter(adata, color=color, title=color,
                 gene_threshold=gene_filter_threshold[0], 
                 count_threshold=count_filter_threshold[0], legend_loc=legend_loc)
    
    
    if not histogram:
        return
    
    if not count_filter_threshold == (0, np.inf):
        print("Counts Threshold")
        # count filtering
        plot_count_filter(adata, obs_col='n_counts', bins=bins,
                          lower = count_threshold[0],
                          filter_lower = count_filter_threshold[0],
                          upper = count_threshold[1],
                          filter_upper = count_filter_threshold[1])

    if not gene_filter_threshold == (0, np.inf):
        print("Gene Threshold")
        # gene filtering
        plot_count_filter(adata, obs_col='n_genes', bins=bins,
                          lower = gene_threshold[0],
                          filter_lower = gene_filter_threshold[0],
                          upper = gene_threshold[1],
                          filter_upper = gene_filter_threshold[1])
        ax.axhline(gene_threshold, 0,1, color='red')
    if count_threshold > 0:
        ax.axvline(count_threshold, 0,1, color='red')
    
    fig = plt.gcf()
    cbar_ax = fig.axes[-1]
    cbar_ax.tick_params(labelsize=tick_size)
    f1 = ax.get_figure()
    plt.show()
    
#Data quality summary plots        
def plot_count_filter(adata, obs_col='n_counts', bins=60, lower=0, upper=np.inf, filter_lower=0, filter_upper=np.inf):
    
    plot_data = adata.obs[obs_col]
    
    sns.distplot(plot_data, kde=False, bins=bins)
    
    if lower > 0:
        plt.axvline(lower, linestyle = '--', color = 'g')
    if filter_lower > 0:
        plt.axvline(filter_lower, linestyle = '-', color = 'r')
    if not np.isinf(upper):
        plt.axvline(upper, linestyle = '--', color = 'g')
    if not np.isinf(upper):
        plt.axvline(filter_upper, linestyle = '-', color = 'r')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
    plt.show()
    
    # determine lower bound of total, look at points below lower bound
    if filter_lower > 0:
        print(f"lower threshold: {filter_lower}")
        sns.distplot(plot_data[plot_data < lower], kde=False, bins=bins)
        plt.axvline(filter_lower, linestyle = '-', color = 'r')
        plt.axvline(lower, linestyle = '--', color = 'g')
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
        plt.show()

    # determine upper bound of total
    if not np.isinf(filter_upper) and not np.isinf(upper):
        print(f"upper threshold: {filter_upper}")
        sns.distplot(plot_data[plot_data > upper], kde=False, bins=bins)
        plt.axvline(filter_upper, linestyle = '-', color = 'r')
        plt.axvline(upper, linestyle = '--', color = 'g')
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
        plt.show()
        
def plot_QC(adata, color=None, bins=60, legend_loc='right margin', histogram=True,
            gene_threshold=(0,np.inf), 
            gene_filter_threshold=(0,np.inf),
            count_threshold=(0,np.inf), 
            count_filter_threshold=(0,np.inf)):
    
    if count_filter_threshold == (0, np.inf):
        count_filter_threshold = count_threshold
    if gene_filter_threshold == (0, np.inf):
        gene_filter_threshold = gene_threshold
    
    # 2D scatter plot
    plot_scatter(adata, color=color, title=color,
                 gene_threshold=gene_filter_threshold[0], 
                 count_threshold=count_filter_threshold[0], legend_loc=legend_loc)
    
    
    if not histogram:
        return
    
    if not count_filter_threshold == (0, np.inf):
        print("Counts Threshold")
        # count filtering
        plot_count_filter(adata, obs_col='n_counts', bins=bins,
                          lower = count_threshold[0],
                          filter_lower = count_filter_threshold[0],
                          upper = count_threshold[1],
                          filter_upper = count_filter_threshold[1])

    if not gene_filter_threshold == (0, np.inf):
        print("Gene Threshold")
        # gene filtering
        plot_count_filter(adata, obs_col='n_genes', bins=bins,
                          lower = gene_threshold[0],
                          filter_lower = gene_filter_threshold[0],
                          upper = gene_threshold[1],
                          filter_upper = gene_filter_threshold[1])

def normalize(adata, color_col='batch', min_mean = 0.1):
    import_rpy2()
    ro.r('library("scran")')
    
    adata_pp = adata.copy()
    sc.pp.normalize_per_cell(adata_pp, counts_per_cell_after=1e6)
    sc.pp.log1p(adata_pp)
    sc.pp.pca(adata_pp, n_comps=15, svd_solver='arpack')
    sc.pp.neighbors(adata_pp)
    sc.tl.louvain(adata_pp, key_added='groups', resolution=0.5)
    
    ro.globalenv['data_mat'] = adata.X.T
    ro.globalenv['input_groups'] = adata_pp.obs['groups']
    size_factors = ro.r(f'computeSumFactors(data_mat, clusters = input_groups, min.mean = {min_mean})')
    
    # modify adata
    adata.obs['size_factors'] = size_factors
    adata.layers["counts"] = adata.X.copy()

    adata.X /= adata.obs['size_factors'].values[:,None]
    sc.pp.log1p(adata)
    adata.raw = adata # Store the full data set in 'raw' as log-normalised data for statistical testing    
    utils.summarize_counts(adata, mito=False) # average counts for normalised counts
    
def reduce_data(adata, subset=False,
                hvg=True, flavor='cell_ranger', n_top_genes=4000, bins=20,
                pca=True,
                neighbors=True, 
                paga=False, paga_groups='batch', 
                umap=True,
                tsne=False,
                diffmap=False,
                draw_graph=False):
    
    
    
    if hvg:
        sc.pp.highly_variable_genes(adata, flavor=flavor, n_top_genes=n_top_genes, n_bins=bins, subset=subset)
        n_hvg = np.sum(adata.var["highly_variable"])
        print(f'\nNumber of highly variable genes: {n_hvg}')
    if pca:
        sc.pp.pca(adata, n_comps=50, use_highly_variable=hvg, svd_solver='arpack')
    sc.pp.neighbors(adata)
    if tsne:
        sc.tl.tsne(adata, n_jobs=12) # n_jobs works for MulticoreTSNE, but not regular implementation
    if umap:
        sc.tl.umap(adata)
    if paga:
        print(f'Compute PAGA by group "{paga_groups}"')
        sc.tl.paga(adata, groups=paga_groups)
    if diffmap:
        sc.tl.diffmap(adata)
    if draw_graph:
        sc.tl.draw_graph(adata)
